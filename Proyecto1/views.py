from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TituloAcademico
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

@login_required
def admin_home_view(request):
    if request.method == 'POST':
        tipo_documento = request.POST.get('tipo_documento')
        numero_documento = request.POST.get('numero_documento')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        carrera = request.POST.get('carrera')
        seccional = request.POST.get('seccional')
        fecha_ingreso = request.POST.get('fecha_ingreso') or None
        fecha_grado = request.POST.get('fecha_grado')

        if TituloAcademico.objects.filter(tipo_documento=tipo_documento, numero_documento=numero_documento).exists():
            messages.error(request, f"Ya existe un título registrado para el documento {tipo_documento} {numero_documento}")
        else:
            nuevo_titulo = TituloAcademico(
                tipo_documento=tipo_documento,
                numero_documento=numero_documento,
                nombres=nombres,
                apellidos=apellidos,
                carrera=carrera,
                seccional=seccional,
                fecha_ingreso=fecha_ingreso,
                fecha_grado=fecha_grado
            )
            nuevo_titulo.save()
            messages.success(request, f"Título de {nombres} {apellidos} registrado exitosamente en el bloque")
        return redirect('admin_home')
    titulos = TituloAcademico.objects.all().order_by('-id')
    return render(request, 'admin_home.html', {'titulos': titulos})

def custom_logout_view(request):
    logout(request)
    return redirect('two_factor:login')

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