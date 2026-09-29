from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    # Login y logout usan las vistas que trae Django; solo se indica el template propio.
    path('ingresar/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('salir/', auth_views.LogoutView.as_view(), name='logout'),
]
