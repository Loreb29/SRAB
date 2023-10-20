from django.db import models
class Estudiantes(models.Model):
    IDent=models.CharField(max_length=40)
    Nombre=models.CharField(max_length=40)
    Carrera=models.CharField(max_length=20)

class ADMIN(models.Model):
    Usuario=models.CharField(max_length=15)
    Contrasena=models.CharField(max_length=30)
    NombreAd=models.CharField(max_length=40)