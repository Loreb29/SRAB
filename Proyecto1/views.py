from django.shortcuts import render
from django.http import JsonResponse
from .models import TituloAcademico
from django.contrib.auth.decorators import login_required

@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

def home(request):
    return render(request, 'index.html')

def consultar_titulo(request):
    tipo_doc = request.GET.get('tipo_doc')
    num_doc = request.GET.get('num_doc')
    if not tipo_doc or not num_doc:
        return JsonResponse({'encontrado': False, 'mensaje': 'Parámetros incompletos'}, status=400)

    try:
        registro = TituloAcademico.objects.get(
            tipo_documento=tipo_doc,
            numero_documento=num_doc
        )
        return JsonResponse({
            'encontrado': True,
            'nombre_completo': f"{registro.nombres} {registro.apellidos}",
            'carrera': registro.carrera,
            'seccional': registro.seccional,
            'fecha_grado': registro.fecha_grado.strftime('%d/%m/%Y'),
            'hash_bloque': registro.hash_bloque
        })
    except TituloAcademico.DoesNotExist:
        return JsonResponse({
            'encontrado': False,
            'mensaje': 'El número de documento no registra ningun titulo de pregrado de la Universidad de Cundinamarca'
        })