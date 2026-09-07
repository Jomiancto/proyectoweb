from django.shortcuts import render


def mostrar_home(request):
    return render(request, 'inicio.html')


def mostrar_acerca(request):
    datos = {
        'nombre': 'ProyectoWeb',
        'descripcion': 'Proyecto Django creado para practicar rutas y plantillas.',
        'rrss': {
            'instagram': '@proyectoweb',
            'github': 'github.com/Jomiancto/proyectoweb',
        },
    }
    return render(request, 'acerca.html', datos)
