"""Rutas principales del proyecto.

Cada app define sus propias rutas en su archivo urls.py, y aquí se incluyen:

- admin/   panel de administración de Django
- (raíz)   páginas generales de la app core, como el inicio
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
