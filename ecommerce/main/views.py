from django.shortcuts import render,redirect
from .models import Product,CustomUser
from .forms import UserForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from cart.cart import Cart
# from wishlist.wishlist import Wishlist
from .decorators import notauthenticated
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
# Create your views here.

def checkverified(user):
    if user.is_authenticated and user.verified == True:
        return True
    else:
        return False

def home(req):
    products=Product.objects.all()
    cart=Cart(req)
    context={
        'products':products,
        'cart':cart,
    }
    return render(req,'index.html',context)
@notauthenticated
def register(req):
    form=UserForm()
    if req.method == "POST":
        form=UserForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.verified= False
            user.save()
            activateEmail(req, user, req.POST.get('email'))
            return redirect('login')
        else:
            messages.error(req,"The values you entered do not match the spectifications, please try again.")

    context={
        'form':form,
    }
    return render(req, 'register.html', context)
@notauthenticated
def userLogin(req):

    if req.method == "POST":
        email=req.POST.get('email')
        password=req.POST.get('password')
        user=authenticate(req,username=email, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            messages.error(req,"Username or password are invalid")

    return render(req, 'login.html')
@login_required(login_url='login')
def userLogout(req):
    user=req.user
    if user.is_authenticated:
        logout(req)
        return redirect('home')
    else:
        return redirect('login')

@login_required(login_url='login')
@user_passes_test(checkverified,login_url='plsver')
def productDetail(req, product_id):
    product=Product.objects.get(id=product_id)
    categories=product.categories.all()
    context={
        'product':product,
        'categories':categories,
    }
    return render(req,'productdetails.html', context)

def verify(req, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.verified = True
        user.save()

        messages.success(req, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(req, "Activation link is invalid!")

    return redirect('home')

def activateEmail(req, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(req).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if req.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(req, f'Dear {user}, please go to your inbox and click on \
                received activation link to confirm and complete the registration. Note: Check your spam folder')
    else:
        messages.error(req, f'Problem sending email to {to_email}, check if you typed it correctly.')

def plsver(req):
    user=req.user
    if user.is_authenticated:
        if user.verified == False:
            messages.error(req,f"Please verify your account with the activation link sent to your email {user.email} before you can start using the website. Note: Check the spam folder if your don't find the email in your inbox")
            return redirect('home')
        else:
            pass
    else:
        return redirect('login')
    
@login_required(login_url='login')
def profile(req):
    user=req.user
    context={
        'user':user,
    }
    return render(req,'profile.html',context)
@login_required(login_url='login')
def updateUser(req):
    if req.method == "POST":
        form=UpdateForm(req.POST, req.FILES, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=UpdateForm(instance=req.user)

        context={
            'form':form,
        }
        return render(req,'updateuser.html',context)
    
@login_required(login_url='login')
@user_passes_test(checkverified,login_url='plsver')
def base(req):
    cart=Cart(req)
    context={
        'cart':cart,
    }
    return HttpResponse(req, 'base.html',context)

def search(req):
    q=req.GET['query']
    products=Product.objects.filter(name__icontains=q)
    cart=Cart(req)
    context={
        'products':products,
        'cart':cart,
    }
    return render(req,'index.html',context)