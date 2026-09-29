from django.shortcuts import render


def inicio(request):
    """Página de inicio del sitio.

    Es pública: la ven tanto visitantes como personas con sesión iniciada.
    El template ajusta los botones según si hay sesión o no.
    """
    return render(request, 'core/inicio.html')
