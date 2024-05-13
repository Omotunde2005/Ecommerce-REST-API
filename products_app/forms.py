from django import forms
from django.contrib.auth.forms import UserCreationForm
from products_app.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "email"]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )