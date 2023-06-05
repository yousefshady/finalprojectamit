from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.views import checkverified
from .cart import Cart
# Create your views here.

@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def addtocart(req, product_id):
    cart=Cart(req)
    cart.add(product_id)

    return redirect('home')
@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def removefromcart(req, product_id):
    cart=Cart(req)
    cart.remove(product_id)

    return redirect('cart')
@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def cartview(req):
    cart= Cart(req)
    context={
        'cart':cart
    }
    return render(req, 'cart.html', context)
@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def changequantity(req, product_id):
    action=req.GET.get('action','')
    if action:
        quantity=1
        if action == 'decrease':
            quantity=-1
        cart=Cart(req)
        cart.add(product_id,quantity,True)
    return redirect('cart')