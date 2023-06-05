from django.db import models
from main.models import Product,CustomUser
# Create your models here.

class Wishlist(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)