from django.test import TestCase
from django.urls import reverse

from .models import User

CONTRASENA = 'clave-segura-2026'


class RegistroTests(TestCase):
    """Pruebas del registro de cuentas nuevas."""

    def datos_validos(self, **cambios):
        datos = {
            'username': 'usuario1',
            'apodo': 'Sam',
            'pronombres': 'elle',
            'email': '',
            'password1': CONTRASENA,
            'password2': CONTRASENA,
        }
        datos.update(cambios)
        return datos

    def test_registro_muestra_formulario(self):
        respuesta = self.client.get(reverse('registro'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Crea tu cuenta')

    def test_registro_valido_crea_usuario_e_inicia_sesion(self):
        respuesta = self.client.post(reverse('registro'), self.datos_validos(), follow=True)
        self.assertRedirects(respuesta, reverse('inicio'))
        usuario = User.objects.get(username='usuario1')
        self.assertEqual(usuario.apodo, 'Sam')
        self.assertTrue(respuesta.context['user'].is_authenticated)
        # La navegación saluda con el apodo
        self.assertContains(respuesta, 'Hola, Sam')

    def test_pronombres_son_opcionales(self):
        self.client.post(reverse('registro'), self.datos_validos(pronombres=''))
        self.assertTrue(User.objects.filter(username='usuario1').exists())

    def test_contrasenas_distintas_no_crean_usuario(self):
        respuesta = self.client.post(reverse('registro'), self.datos_validos(password2='otra-clave-2026'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(User.objects.filter(username='usuario1').exists())

    def test_apodo_es_obligatorio(self):
        self.client.post(reverse('registro'), self.datos_validos(apodo=''))
        self.assertFalse(User.objects.filter(username='usuario1').exists())


class IngresoSalidaTests(TestCase):
    """Pruebas de iniciar y cerrar sesión."""

    def setUp(self):
        User.objects.create_user(username='usuario1', password=CONTRASENA, apodo='Sam')

    def test_login_valido_redirige_al_inicio(self):
        respuesta = self.client.post(reverse('login'), {'username': 'usuario1', 'password': CONTRASENA})
        self.assertRedirects(respuesta, reverse('inicio'))

    def test_login_invalido_muestra_error(self):
        respuesta = self.client.post(reverse('login'), {'username': 'usuario1', 'password': 'incorrecta'})
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(respuesta.context['user'].is_authenticated)

    def test_logout_cierra_la_sesion(self):
        self.client.login(username='usuario1', password=CONTRASENA)
        respuesta = self.client.post(reverse('logout'), follow=True)
        self.assertFalse(respuesta.context['user'].is_authenticated)
        self.assertContains(respuesta, 'Ingresar')
