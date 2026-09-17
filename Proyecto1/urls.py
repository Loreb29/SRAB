from django.contrib import admin
from django.urls import path, include
from .views import home, consultar_titulo, admin_home_view, custom_logout_view
from two_factor.urls import urlpatterns as tf_urls


urlpatterns = [
    path('', home, name='home'),
    path('api/consultar/', consultar_titulo, name='consultar_titulo'),
    path('admin/home/', admin_home_view, name='admin_home'),
    path('logout/', custom_logout_view, name='logout'),
    path('', include(tf_urls, 'two_factor')),
    path('admin/', admin.site.urls),
]