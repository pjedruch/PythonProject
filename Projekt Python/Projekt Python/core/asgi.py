import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
#Kod służy do uruchamiania aplikacji Django za pomocą ASGI (Asynchronous Server Gateway Interface), 
#która umożliwia obsługę żądań asynchronicznie.