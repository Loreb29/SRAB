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
    noombre=''
    nombres=''
    caarrera=''
    carreras=''
    if request.method=='POST':
        num=request.POST.get("entrada")
    if num!='':
        try:
            for noombre in Estudiantes.objects.raw(("SELECT Nombre as id FROM srab.datos_estudiantes WHERE IDent =%s;")%num):
                noombre=str(noombre)
        except django.db.utils.OperationalError:
            nose="queponer"
        try:
            for caarrera in Estudiantes.objects.raw(("SELECT Carrera as id FROM srab.datos_estudiantes WHERE IDent =%s;")%num):
                caarrera=str(caarrera)
        except django.db.utils.OperationalError:
            nose="queponer" 
    if noombre!='':
        #ids=id[20]
        #if ids=='1':
        #    Nombre="Juan"
        #    Apellido="Lopez"
        #    Carrera="Ingenieria de Sistemas"
        #    FIngreso="01/02/2020"
        #    FGraduacion="14/11/2025"
        #    Sede="Ubate"
        ran1=len(noombre)
        ran2=len(caarrera)
        for elemento in range(20,(ran1-1)):
            nombres=nombres+noombre[elemento]
        for elemento in range(20,(ran2-1)):
            carreras=carreras+caarrera[elemento]
        Nombre=nombres
        if carreras=="Ig":
            carreras="Ingenieria de Sistemas"
        elif carreras=="Zoo":
            carreras="Zootecnia"
        elif carreras=="Igc":
            carreras="Ingenieria de Sistemas y Computación"
        elif carreras=="Mu":
            carreras="Musica"
        Carrera=carreras
    lista={"Nombre":Nombre,"Apellido":Apellido,"Carrera":Carrera,"Ingreso":FIngreso,"Graduacion":FGraduacion,"Sede":Sede}
    return render(request,'static/ID/indexBusc.html',lista)

def inicio(request):
    return render(request,'static/admin/indexAdd.html')


def subir(request):
    return render(request,'static/admin/indexLogin.html')

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


