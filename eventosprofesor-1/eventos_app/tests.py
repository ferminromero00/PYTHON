from django.test import TestCase
from .models import Evento
from django.contrib.auth import get_user_model

User = get_user_model()

class EventoModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.evento = Evento.objects.create(
            titulo='Evento de Prueba',
            descripcion='Descripción del evento de prueba',
            fecha='2023-10-01',
            usuario_creador=self.user
        )

    def test_evento_creation(self):
        self.assertEqual(self.evento.titulo, 'Evento de Prueba')
        self.assertEqual(self.evento.descripcion, 'Descripción del evento de prueba')
        self.assertEqual(self.evento.fecha, '2023-10-01')
        self.assertEqual(self.evento.usuario_creador, self.user)

    def test_evento_str(self):
        self.assertEqual(str(self.evento), 'Evento de Prueba')

class EventoViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_index_view(self):
        response = self.client.get('/eventos/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos_app/index.html')

    def test_crear_evento_view(self):
        response = self.client.post('/eventos/crear/', {
            'titulo': 'Nuevo Evento',
            'descripcion': 'Descripción del nuevo evento',
            'fecha': '2023-10-02'
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        self.assertTrue(Evento.objects.filter(titulo='Nuevo Evento').exists())

    def test_borrar_evento_view(self):
        evento = Evento.objects.create(
            titulo='Evento a Borrar',
            descripcion='Descripción del evento a borrar',
            fecha='2023-10-03',
            usuario_creador=self.user
        )
        response = self.client.post(f'/eventos/borrar/{evento.id}/')
        self.assertEqual(response.status_code, 302)  # Redirige después de borrar
        self.assertFalse(Evento.objects.filter(id=evento.id).exists())