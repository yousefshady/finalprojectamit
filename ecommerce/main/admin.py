from django.contrib import admin
from .models import Product,CustomUser,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Category)