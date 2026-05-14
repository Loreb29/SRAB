from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datos.models import Estudiantes, ADMIN
import random
import json
import urllib.request
from django.contrib.auth.hashers import check_password

def BUSCADOR(request):
    context = {}
    if request.method == 'POST':
        num = request.POST.get("entrada")
        if num:
            estudiante = Estudiantes.objects.filter(IDent=num).first()
            if estudiante:
                carrera = estudiante.Carrera
                if carrera == "Ig":
                    carrera = "Ingenieria de Sistemas"
                elif carrera == "Zoo":
                    carrera = "Zootecnia"
                elif carrera == "Cont":
                    carrera = "Contaduria"
                elif carrera == "Igc":
                    carrera = "Ingenieria de Sistemas y Computación"
                elif carrera == "Mu":
                    carrera = "Musica"
                
                context = {
                    "Nombre": estudiante.Nombre,
                    "Carrera": carrera,
                }
            else:
                context = {"not_found": True}
                
    return render(request, 'static/ID/indexBusc.html', context)

def inicio(request):
    if request.method == 'POST':
        user = request.POST.get("username")
        password_input = request.POST.get("password")
        if user and password_input:
            admin_user = ADMIN.objects.filter(Usuario=user).first()
            if admin_user:
                request.session['admin_auth'] = True
                request.session['admin_name'] = admin_user.NombreAd
                return redirect('admin_menu')
            else:
                return render(request, 'static/admin/indexLogin.html', {"error": True})
                
    return render(request, 'static/admin/indexLogin.html')

def subir(request):
    admin_name = request.session.get('admin_name', 'Admin')
    context = {"Nombre": admin_name}
    
    if request.method == 'POST':
        cedula = request.POST.get("cedula")
        nombre = request.POST.get("nombre")
        carreras = request.POST.get('carreras', None)
        
        carrera = ""
        if carreras == "1":
            carrera = "Ig"
        elif carreras == "2":
            carrera = "Igc"
        elif carreras == "3":
            carrera = "Mu"
            
        if cedula and nombre and carrera:
            Estudiantes.objects.create(IDent=cedula, Nombre=nombre, Carrera=carrera)
            context["success"] = True
            
    return render(request, 'static/admin/indexAdd.html', context)

def SRAB(request):
    h = str(random.randint(1, 5))
    nombres = ["Jose", "Julian", "Ibrahim", "Bahir", "Julio", "Andres"]
    apellidos = ["Navarrete", "Niño", "Gonzales", "Sierra"]
    
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    while a == b:
        a = random.randint(0, 5)
        
    c = random.randint(0, 3)
    d = random.randint(0, 3)
    while c == d:
        d = random.randint(0, 3)
        
    u = random.randint(0, 1)
    lugar = "Ubaté" if u == 1 else "Fusagasugá"
    
    lista = {
        "nombre1": nombres[a],
        "nombre2": nombres[b],
        "apellido1": apellidos[c],
        "apellido2": apellidos[d],
        "fin1": str(random.randint(0, 9)),
        "fin2": str(random.randint(21, 35)),
        "lugar": lugar,
        "nombre": "",
        "clave": "",
        "num": h
    }
    return render(request, 'indexPrincipal.html', lista)

@csrf_exempt
def chat_gemini(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        body = json.loads(request.body)
        user_message = body.get('message', '').strip()
        history = body.get('history', [])
        lang = body.get('lang', 'es')
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({'error': 'Invalid request body'}, status=400)

    if not user_message:
        return JsonResponse({'error': 'Empty message'}, status=400)

    api_key = getattr(settings, 'GEMINI_API_KEY', '')
    if not api_key or api_key == 'YOUR_GEMINI_API_KEY_HERE':
        return JsonResponse({'reply': 'La clave de API de Gemini no está configurada. Por favor contacta al administrador del sistema.'}, status=200)

    contents = []
    for msg in history:
        role = msg.get('role')
        text = msg.get('text', '')
        if role in ('user', 'model') and text:
            contents.append({'role': role, 'parts': [{'text': text}]})
    contents.append({'role': 'user', 'parts': [{'text': user_message}]})

    udec_motto = (
        'Soy LIBRE, AUTÓNOMO Y RESPONSABLE a través del diálogo y la construcción, '
        'como ideal regulativo; me dirijo, controlo y dicto mis propias leyes.'
    )

    if lang == 'en':
        system_instruction = (
            'You are a customer support assistant for the SRAB system (Sistema de Registro y Acreditación de Beneficiarios) '
            'at the Universidad de Cundinamarca. Your role is to help users with questions about ID document searches, '
            'accepted document types, available degree programs, and general system usage. '
            'Always respond in English, in a friendly and concise manner. '
            f'The guiding principle of the Universidad de Cundinamarca is: "{udec_motto}" — '
            'Let this spirit of freedom, autonomy and responsibility guide the tone and values of your responses.'
        )
    else:
        system_instruction = (
            'Eres un asistente de soporte al cliente del sistema SRAB (Sistema de Registro y Acreditación de Beneficiarios) '
            'de la Universidad de Cundinamarca. Tu función es ayudar a los usuarios con dudas sobre la búsqueda de cédulas, '
            'tipos de documentos aceptados, carreras disponibles y el uso general del sistema. '
            'Responde siempre en español, de forma amable y concisa. '
            f'El principio rector de la Universidad de Cundinamarca es: "{udec_motto}" — '
            'Deja que este espíritu de libertad, autonomía y responsabilidad guíe el tono y los valores de tus respuestas.'
        )

    model_fallback = [
        'gemini-2.5-flash',
        'gemini-flash-latest',
        'gemini-2.5-flash-lite',
        'gemini-2.0-flash',
    ]

    payload_data = {
        'system_instruction': {'parts': [{'text': system_instruction}]},
        'contents': contents,
        'generationConfig': {'maxOutputTokens': 512, 'temperature': 0.7}
    }

    reply = None
    last_error = 'No models available.'

    for model in model_fallback:
        payload = json.dumps(payload_data).encode('utf-8')
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode('utf-8'))
            reply = data['candidates'][0]['content']['parts'][0]['text']
            break
        except urllib.error.HTTPError as e:
            last_error = e.read().decode('utf-8')
            continue
        except Exception as e:
            last_error = str(e)
            continue

    if reply is None:
        return JsonResponse({'error': f'All models failed. Last error: {last_error}'}, status=502)

    return JsonResponse({'reply': reply})