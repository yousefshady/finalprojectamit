from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','phone','password1','password2']

class UpdateForm(UserChangeForm):
    password=None
    class Meta:
        model=CustomUser
        fields=["username", "email", "phone"]
        exclude=["password1","password2"]
