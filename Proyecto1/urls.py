from django.urls import path
from .views import home, consultar_titulo

urlpatterns = [
    path('', home, name='home'),
    path('api/consultar/', consultar_titulo, name='consultar_titulo'),
]