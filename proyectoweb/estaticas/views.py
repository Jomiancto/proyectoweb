from django.shortcuts import render


def mostrar_home(request):
    return render(request, 'inicio.html')


def mostrar_acerca(request):
    datos = {
        'wifi': '300mbps',
        'enchufes': 10,
        'cafe': 'Tostado',
        'ambiente': 'Silencioso',
    }
    return render(request, 'acerca.html', datos)
