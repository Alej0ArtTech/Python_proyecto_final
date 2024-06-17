from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm_(AuthenticationForm):
    class Meta:
        model = User
        field = ["username", "password", ] 