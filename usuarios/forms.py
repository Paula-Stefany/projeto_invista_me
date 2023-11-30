from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class CustomUserEditForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email']
