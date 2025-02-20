import os
import sys

from django.core.wsgi import get_wsgi_application

# Añadir la ruta del proyecto al sistema
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventosprofesor.settings')

application = get_wsgi_application()