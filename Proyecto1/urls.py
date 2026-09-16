from django.contrib import admin
from django.urls import path, include
from .views import home, consultar_titulo, admin_home
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path('', home, name='home'),
    path('api/consultar/', consultar_titulo, name='consultar_titulo'),
    path('', include(tf_urls)),
    path('admin/home/', admin_home, name='admin_home'),
    path('admin/', admin.site.urls),
    
    #path('admin/login', LoginView.as_view(), name='login'),
]