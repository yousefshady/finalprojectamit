from django.contrib import admin
from .models import Orders, OrderItem

# Register your models here.

admin.site.register(Orders)
admin.site.register(OrderItem)