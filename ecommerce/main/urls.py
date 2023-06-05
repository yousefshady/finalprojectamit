from django.urls import path
from . import views
from cart.views import addtocart,cartview,removefromcart,changequantity
from wishlist.views import addtowishlist,wishlistview, removefromwishlist
from orders.views import checkout,ordersview,cancelorder,uncancelorder
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Account related
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('verifyemail/<uidb64>/<token>', views.verify, name='verify'),
    path('activateemail/', views.activateEmail, name='activem'),
    path('pleasever/', views.plsver, name='plsver'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.updateUser, name='updateuser'),
    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name="resetpass/reset.html",html_email_template_name="resetpass/emailtem.html", subject_template_name="resetpass/email_subject.txt"), name="resetpass"),
    path('resetpasssent/', auth_views.PasswordResetDoneView.as_view(template_name="resetpass/done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetpass/resetform.html'), name="password_reset_confirm"),
    path('resetpasscomplete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetpass/complete.html'), name="password_reset_complete"),
    # Product related
    path('detailed/<str:product_id>/', views.productDetail, name='detailed'),
    path('search/', views.search, name='search'),
    # Sub: Cart
    path('cart/', cartview, name='cart'),
    path('addtocart/<str:product_id>/', addtocart, name='addtocart'),
    path('removefromcart/<str:product_id>/', removefromcart, name='removefromcart'),
    path('changequantity/<str:product_id>/', changequantity, name='changequantity'),
    path('checkout/',checkout,name='checkout'),
    path('orders/',ordersview,name='orders'),
    path('orders/cancel/<str:order_id>/',cancelorder,name='cancelorder'),
    path('orders/uncancel/<str:order_id>/',uncancelorder,name='uncancelorder'),
    # Sub: Wishlist
    path('wishlist/', wishlistview, name='wishlist'),
    path('addtowishlist/<str:product_id>/', addtowishlist, name='addtowishlist'),
    path('removefromwishlist/<str:product_id>/', removefromwishlist, name='removefromwishlist'),
]
