"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SRAB/', views.SRAB, name='srab_home'),
    path('SRAB/Buscador/', views.BUSCADOR, name='buscador'),
    path('SRAB/Buscador', views.BUSCADOR),
    path('SRAB/Buscador/chat/', views.chat_gemini, name='chat_gemini'),
    path('SRAB/Admin/', views.inicio, name='admin_login'),
    path('SRAB/Admin', views.inicio),
    path('SRAB/Admin/Menu/', views.subir, name='admin_menu'),
    path('SRAB/Admin/Menu', views.subir),
]
