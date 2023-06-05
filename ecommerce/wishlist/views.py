from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from main.views import checkverified

from .models import Wishlist
from main.models import Product

# Create your views here.


@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def addtowishlist(req, product_id):
    pid=Product.objects.get(id=product_id)
    try:
        isin=Wishlist.objects.get(user=req.user, product=pid)
        if isin:
            Wishlist.objects.filter(user=req.user, product=pid).delete()
    except:
        Wishlist.objects.create(user=req.user, product=pid)

    return redirect('home')
@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def removefromwishlist(req, product_id):
    pid=Product.objects.get(id=product_id)
    Wishlist.objects.filter(product=pid).delete()

    return redirect('wishlist')
@user_passes_test(checkverified, login_url='plsver')
@login_required(login_url='login')
def wishlistview(req):
    wishlist= Wishlist.objects.filter(user=req.user)
    context={
        'wishlist':wishlist
    }
    return render(req, 'wishlist.html', context)