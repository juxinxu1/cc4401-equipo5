from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistroForm(UserCreationForm):
    """Formulario para crear una cuenta nueva.

    Extiende el UserCreationForm de Django, que ya valida que las dos
    contraseñas coincidan y que cumplan las reglas de seguridad, y guarda la
    contraseña encriptada. Se agregan los campos propios del modelo User.
    No se pide nombre legal ni género: no son necesarios para usar la aplicación.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'apodo', 'pronombres', 'email')
        labels = {
            'username': 'Nombre de usuario',
            'apodo': '¿Cómo quieres que te llamemos?',
            'pronombres': 'Pronombres',
            'email': 'Correo electrónico (opcional)',
        }
