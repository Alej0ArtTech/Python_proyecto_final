from django.urls import path
from . import views
from .views import CustomLoginView, index
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static




app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="core/logged_out.html"), name='logout'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('productos/', include('productos.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)