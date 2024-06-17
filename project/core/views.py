from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm_

def index(request):
    return render(request, 'core/index.html')

class CustomLoginView(LoginView):
    authentication_form = LoginForm_
    template_name = "core/login.html"

def logged_out(request):
    return render(request, 'core/logged_out.html')