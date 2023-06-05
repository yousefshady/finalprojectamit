from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import Orders,OrderItem
from django.conf import settings
from .forms import OrderForm
from django.contrib.auth.decorators import login_required, user_passes_test
from main.views import checkverified
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.

@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def checkout(req):
    cart=Cart(req)
    form=OrderForm()
    user=req.user
    company_name='Company name here'
    if req.method == "POST":
        form=OrderForm(req.POST)
        if form.is_valid():
            total_cost=0
            for item in cart:
                product=item['product']
                total_cost += product.price * int(item['quantity'])
            order=form.save(commit=False)
            order.user=req.user
            order.total_cost=total_cost
            order.save()
            email = EmailMessage('Order has been placed', f'Dear {user}, your order has been placed. Thank your for choosing {company_name}', to=[user.email])
            email.send()
            for item in cart:
                product=item['product']
                quantity=int(item['quantity'])
                price=product.price * quantity
                item=OrderItem.objects.create(order=order,product=product,price=price,quantity=quantity)
            
            return redirect('cart')

    context={
        'cart':cart,
        'form':form,
    }
    return render(req,'checkout.html',context)

def ordersview(req):
    user=req.user
    orders=Orders.objects.filter(user=user)
    orderitems=OrderItem.objects.filter(order__in=orders)

    context={
        'orders':orders,
        'orderitems':orderitems,
    }
    return render(req,'orders.html',context)

def cancelorder(req, order_id):
    orderid=order_id
    order=Orders.objects.get(id=orderid)
    user=req.user
    company_name='Company name here'
    if order.shipping_status == 'shipped':
        messages.error(req,'Sorry you cannot cancel your order since it has already been shipped')
        return redirect('orders')
    elif order.shipping_status == 'delivered':
        messages.error(req,'Sorry you cannot cancel your order since it has already been delivered')
        return redirect('orders')
    else:
        Orders.objects.filter(id=orderid).update(status='cancelled')
        messages.success(req,'Order cancelled successfully')
        email = EmailMessage('Order has been cancelled', f'Dear {user}, your order has been cancelled. Thank your for choosing {company_name}', to=[user.email])
        email.send()

        return redirect('orders')

def uncancelorder(req, order_id):
    orderid=order_id
    order=Orders.objects.filter(id=orderid)
    user=req.user
    company_name='Company name here'
    order.update(status='ordered')
    messages.success(req,'Order uncancelled successfully')
    email = EmailMessage('Order has been uncancelled', f'Dear {user}, your order has been uncancelled. Thank your for choosing {company_name}', to=[user.email])
    email.send()
    return redirect('orders')