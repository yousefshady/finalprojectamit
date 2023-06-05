from django.forms import ModelForm
from .models import Orders

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=('first_name','last_name', 'address', 'city','neighborhood','zipcode','email','phone','payment_method')