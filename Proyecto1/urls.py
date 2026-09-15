from django.urls import path
from .views import home, consultar_titulo
from two_factor.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('api/consultar/', consultar_titulo, name='consultar_titulo'),
    path('admin/login', LoginView.as_view(), name='login'),
]