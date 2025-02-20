# EventosProfesor

EventosProfesor es una aplicación web desarrollada con Django que permite a los usuarios gestionar eventos y sus invitaciones. A continuación se describen las principales funcionalidades de la aplicación:

## Funcionalidades

### Autenticación de Usuarios
- Los usuarios pueden iniciar sesión en la aplicación.
- Los usuarios pueden cerrar sesión.

### Gestión de Eventos
- Los usuarios pueden crear nuevos eventos.
- Los usuarios pueden ver una lista de sus eventos.
- Los usuarios pueden editar eventos existentes.
- Los usuarios pueden eliminar eventos.

### Invitaciones a Eventos
- Los usuarios pueden invitar a otros usuarios a sus eventos.
- Los usuarios pueden ver y gestionar las invitaciones a sus eventos.
- Los usuarios pueden eliminar invitaciones.
- Los usuarios pueden ver los eventos a los que han sido invitados.

## Modelos
- **Evento**: Incluye campos para el título, descripción, fecha, usuario creador y usuarios invitados.
- **Usuario**: Modelo de usuario personalizado para la autenticación.

## Formularios
- **EventoForm**: Utilizado para la creación y edición de eventos.

## Plantillas
La aplicación utiliza varias plantillas HTML para renderizar las vistas, incluyendo:
- `base.html`
- `index.html`
- `nuevoevento.html`
- `invitados.html`
- `misinvitaciones.html`

## Administración
Los modelos Evento y Usuario están registrados en el sitio de administración de Django, lo que permite gestionar estos modelos a través de la interfaz de administración.

## Instalación
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Realiza las migraciones con `python manage.py migrate`.
4. Inicia el servidor con `python manage.py runserver`.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request.