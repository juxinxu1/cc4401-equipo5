from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Panel de administración del usuario propio.

    Reutiliza el UserAdmin de Django y le agrega una sección con los campos
    nuevos (apodo y pronombres), tanto al editar como al crear usuarios.
    """

    fieldsets = UserAdmin.fieldsets + (
        ('Perfil', {'fields': ('apodo', 'pronombres')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil', {'fields': ('apodo', 'pronombres')}),
    )
    list_display = ('username', 'apodo', 'email', 'is_staff')
