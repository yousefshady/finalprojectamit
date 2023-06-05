from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User system

class CustomUser(AbstractUser):
    username=models.CharField(max_length=150,unique=True,null=True,blank=True)
    email=models.EmailField(unique=True)
    phone=models.IntegerField(unique=True,null=True,blank=True,default=None)
    verified=models.BooleanField(default=False)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.email
    


#product things
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    price=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    categories=models.ManyToManyField(Category, blank=True)
    thumbnail=models.ImageField(upload_to='productthumbnail/')
    sale_price=models.IntegerField(blank=True, null=True, default=0)


    def __str__(self):
        return self.name