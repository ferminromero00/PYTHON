from django.test import TestCase
from django.urls import reverse
from .models import Usuario

class UsuarioModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_usuario_creado(self):
        self.assertEqual(self.usuario.username, 'testuser')
        self.assertTrue(self.usuario.check_password('testpassword'))

class UsuarioViewsTest(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios_app/login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('salir'))
        self.assertEqual(response.status_code, 302)  # Redirige después de cerrar sesión

    def test_usuario_creacion(self):
        response = self.client.post(reverse('crear_usuario'), {
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear usuario
        self.assertTrue(Usuario.objects.filter(username='newuser').exists())