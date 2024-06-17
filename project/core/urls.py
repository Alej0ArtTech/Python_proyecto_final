from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="core/logged_out.html"), name='logout'),
    path('logged_out/', views.logged_out, name='logged_out'),
]