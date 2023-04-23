import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

#kod to plik konfiguracyjny WSGI, który ustawia ustawienia dla aplikacji Django.
#W linii 3 importujemy funkcję get_wsgi_application() z modułu django.core.wsgi. 
#Następnie w linii 5 ustawiamy środowiskową zmienną DJANGO_SETTINGS_MODULE na wartość 'core.settings'. 
#Jest to ścieżka do modułu konfiguracyjnego Django dla naszej aplikacji.
#W linii 7 wywołujemy funkcję get_wsgi_application() i przypisujemy ją do zmiennej application. 
#Ta funkcja zwraca obiekt aplikacji WSGI, który jest odpowiedzialny za obsługę żądań HTTP w naszej aplikacji Django.