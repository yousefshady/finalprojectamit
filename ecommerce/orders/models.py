from django.db import models
from main.models import CustomUser,Product
from cart.cart import Cart

# Create your models here.
class Orders(models.Model):
    PENDING='pending'
    SHIPPED='shipped'
    DELIVERED='delivered'
    ORDERED='ordered'
    CANCELLED='cancelled'
    COD='COD'
    VISAOD='visa'
    SHIP_STATUSES=[
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
    ]
    ORDER_STATUSES=[
        (ORDERED, 'Ordered'),
        (CANCELLED, 'Cancelled'),
    ]
    PAYMENT_METHOD=[
        (COD, 'Cash on delivery'),
        (VISAOD, 'Visa on delivery')
    ]

    user=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    address=models.TextField()
    city=models.CharField(max_length=300)
    neighborhood=models.CharField(max_length=300)
    zipcode=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    total_cost=models.IntegerField(default=0)
    paid=models.BooleanField(default=False)
    shipping_status=models.CharField(max_length=20,choices=SHIP_STATUSES, default=PENDING)
    status=models.CharField(max_length=20, choices=ORDER_STATUSES, default=ORDERED)
    payment_method=models.CharField(max_length=30, choices=PAYMENT_METHOD, default=COD)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.email}"

class OrderItem(models.Model):
    order=models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order.first_name} {self.order.last_name}'s order"