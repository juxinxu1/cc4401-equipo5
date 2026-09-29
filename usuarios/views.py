from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegistroForm


def registro(request):
    """Crea una cuenta nueva.

    - GET: muestra el formulario vacío.
    - POST: valida los datos; si son correctos crea el usuario, inicia su
      sesión y lo lleva al inicio. Si hay errores, vuelve a mostrar el
      formulario con los datos ya ingresados y los mensajes de error.
    """
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'Tu cuenta quedó creada. Te damos la bienvenida, {usuario.nombre_visible()}.')
            return redirect('inicio')
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})
