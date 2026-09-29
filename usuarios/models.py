from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Usuario del sistema.

    Hereda de AbstractUser, así que mantiene todo lo que trae el usuario de
    Django (username, contraseña, email, permisos, etc.) y agrega dos campos:

    - apodo: nombre con el que la aplicación se dirige a la persona. Se muestra
      en lugar del nombre legal, que no se pide.
    - pronombres: opcionales y de texto libre, para que cada persona los escriba
      como prefiera en vez de elegir de una lista cerrada.
    """

    apodo = models.CharField(
        'apodo',
        max_length=30,
        help_text='Es el nombre con el que te vamos a llamar dentro de la aplicación.',
    )
    pronombres = models.CharField(
        'pronombres',
        max_length=30,
        blank=True,
        help_text='Opcional. Los usamos solo para referirnos a ti correctamente (ej.: ella, él, elle).',
    )

    def nombre_visible(self):
        """Devuelve el nombre que se muestra en la interfaz: el apodo, o el username si no hay apodo."""
        return self.apodo or self.username

    def __str__(self):
        return self.nombre_visible()
