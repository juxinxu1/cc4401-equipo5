from django.test import TestCase
from django.urls import reverse


class InicioTests(TestCase):
    """Pruebas de la página de inicio."""

    def test_inicio_responde_para_visitantes(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Te damos la bienvenida')

    def test_inicio_ofrece_crear_cuenta_a_visitantes(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertContains(respuesta, reverse('registro'))
        self.assertContains(respuesta, reverse('login'))
