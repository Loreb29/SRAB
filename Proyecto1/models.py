import hashlib
from django.db import models

class TituloAcademico(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PAS', 'Pasaporte'),
    ]

    tipo_documento = models.CharField(
        max_length=3, 
        choices=TIPO_DOCUMENTO_CHOICES,
        verbose_name="Tipo de Documento"
    )
    numero_documento = models.CharField(
        max_length=20, 
        db_index=True, 
        verbose_name="Número de Documento"
    )
    
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    carrera = models.CharField(max_length=150, verbose_name="Carrera / Programa Académico")
    seccional = models.CharField(
        max_length=100, 
        verbose_name="Seccional / Sede",
        help_text="Ej: Sede Fusagasugá, Seccional Girardot, Extensión Ubaté, etc."
    )
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso", null=True, blank=True)
    fecha_grado = models.DateField(verbose_name="Fecha de Graduación / Salida")
    hash_bloque = models.CharField(
        max_length=64, 
        unique=True,
        blank=True,
        verbose_name="Hash del Bloque Blockchain",
        help_text="Hash criptográfico inmutable que identifica el título en la cadena de bloques."
    )
    hash_anterior = models.CharField(
        max_length=64, 
        verbose_name="Hash del Bloque Anterior",
        null=True, 
        blank=True
    )
    
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Título Académico"
        verbose_name_plural = "Títulos Académicos"
        unique_together = ('tipo_documento', 'numero_documento')

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.carrera} ({self.tipo_documento}: {self.numero_documento})"

    def save(self, *args, **kwargs):
        if not self.hash_bloque:
            ultimo_registro = TituloAcademico.objects.order_by('-id').first()
            if ultimo_registro:
                self.hash_anterior = ultimo_registro.hash_bloque
            else:
                self.hash_anterior = "0"*64

            cadena_datos = f"{self.tipo_documento}{self.numero_documento}{self.nombres}{self.apellidos}{self.carrera}{self.fecha_grado}{self.hash_anterior}"
            self.hash_bloque = hashlib.sha256(cadena_datos.encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)                    