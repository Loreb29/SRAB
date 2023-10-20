from calendar import c
from re import A
from tkinter import N
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render,redirect
from datos.models import Estudiantes
import random
import datetime
import os
def BUSCADOR(request):
    est=Estudiantes(IDent=10000162190,Nombre='Juan',Carrera='IngSis')
    est.save();
    
    return render(request,'static/ID/index.html')

def SRAB(request):
    h=random.randint(1,5)
    h=str(h)
    cero=0
    nombres=["Jose","Julian","Ibrahim","Bahir","Julio","Andres"]
    apellidos=["Navarrete","Niño","Gonzales","Sierra"]
    a=random.randint(0,5)
    b=random.randint(0,5)
    u=random.randint(0,1)
    if u==1:
        lugar="Ubaté"
    else:
        lugar="Fusagasugá"
    while a==b:
        a=random.randint(0,5)
    nombre=""
    clave=""
    c=random.randint(0,3)
    d=random.randint(0,3)
    while c==d:
        d=random.randint(0,3)
    nombre1=nombres[a]
    nombre2=nombres[b]
    apellido1=apellidos[c]
    apellido2=apellidos[d]
    fin1=random.randint(0,9)
    fin1=str(fin1)
    fin2=random.randint(21,35)
    fin2=str(fin2)
    lista={"nombre1":nombre1,"nombre2":nombre2,"apellido1":apellido1,"apellido2":apellido2,"fin1":fin1,"fin2":fin2,"lugar":lugar,"nombre":nombre,"clave":clave,"num":h}
    return render(request,'index.html',lista)


