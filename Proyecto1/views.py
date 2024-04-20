from calendar import c
from re import A
from tkinter import N
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render,redirect
from datos.models import Estudiantes
import django.db.utils
import random
def BUSCADOR(request):
    num=''
    Nombre=''
    Apellido=''
    Carrera=''
    FIngreso=''
    FGraduacion=''
    Sede=''
    id=''
    ids=''
    if request.method=='POST':
        num=request.POST.get("entrada")
    cambios=0
    if num!='':
        try:
            for id in Estudiantes.objects.raw(("SELECT id FROM srab.datos_estudiantes WHERE IDent =%s;")%num):
                id=str(id)
        except django.db.utils.OperationalError:
            nose="queponer"
    if id!='':
        ids=id[20]
        if ids=='1':
            Nombre="Juan"
            Apellido="Lopez"
            Carrera="Ingenieria de Sistemas"
            FIngreso="01/02/2020"
            FGraduacion="14/11/2025"
            Sede="Ubate"
        elif ids=='2':
            Nombre="Julio"
            Apellido="Morales"
            Carrera="Ingenieria de Sistemas"
            FIngreso="01/02/2019"
            FGraduacion="14/11/2024"
            Sede="Ubate" 
        elif ids=='3':
            Nombre="Ana"
            Apellido="Robledo"
            Carrera="Zootecnia"
            FIngreso="14/08/2012"
            FGraduacion="15/07/2018"
            Sede="Ubate"
        elif ids=='4':
            Nombre="Bahir"
            Apellido="Rocha"
            Carrera="Ingenieria de Sistemas y Computación"
            FIngreso="14/08/2010"
            FGraduacion="15/07/2017"
            Sede="Fusagasuga"
        elif ids=='5':
            Nombre="Ramiro"
            Apellido="Gonzales"
            Carrera="Musica"
            FIngreso="15/07/2021"
            FGraduacion="01/02/2026"
            Sede="Zipaquira"
        elif ids=='6':
            Nombre="Maria"
            Apellido="Niño"
            Carrera="Musica"
            FIngreso="01/02/2020"
            FGraduacion="14/11/2025"
            Sede="Zipaquira"
        else:
            ids=''
            cambios=1
            print(Nombre)
    lista={"Nombre":Nombre,"Apellido":Apellido,"Carrera":Carrera,"Ingreso":FIngreso,"Graduacion":FGraduacion,"Sede":Sede,"id":ids}
    return render(request,'static/ID/indexBusc.html',lista)

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
    return render(request,'indexPrincipal.html',lista)


