import os
from pathlib import Path
#Zmienna BASE_DIR definiuje ścieżkę do katalogu głównego projektu.
BASE_DIR = Path(__file__).resolve().parent.parent
#Zmienna SECRET_KEY zawiera klucz tajny używany przez Django do generowania tokenów CSRF i innych celów bezpieczeństwa.
SECRET_KEY = 'django-insecure-i5in%d2lr$fsjt9ge$uwro=u=*c(5hl=@_=e#f9i!kfo4s)u(!'
#Zmienna DEBUG włącza tryb debugowania aplikacji.
DEBUG = True
#Zmienna ALLOWED_HOSTS określa listę dozwolonych hostów, które mogą obsługiwać aplikację.
ALLOWED_HOSTS = ['yourdomain.com','127.0.0.1','localhost']
#Zmienna INSTALLED_APPS zawiera listę zainstalowanych aplikacji Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'users',
    'orders',
    'payment',
]
#Zmienna MIDDLEWARE definiuje listę pośredników, które są używane przez Django do przetwarzania żądań HTTP.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#Zmienna ROOT_URLCONF określa plik URL głównego projektu
ROOT_URLCONF = 'core.urls'
#Zmienna TEMPLATES definiuje ustawienia dla silnika szablonów.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'cart.context_processors.cart'
            
            ],
        },
    },
]
#Zmienna WSGI_APPLICATION określa plik WSGI głównego projektu.
WSGI_APPLICATION = 'core.wsgi.application'
#Zmienna DATABASES zawiera ustawienia połączenia z bazą danych
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#Zmienna AUTH_PASSWORD_VALIDATORS zawiera listę walidatorów hasła użytkownika
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#Zmienna LANGUAGE_CODE określa język, który ma być używany w aplikacji.
LANGUAGE_CODE = 'pl'
# Zmienna TIME_ZONE określa strefę czasową dla aplikacji.
TIME_ZONE = 'UTC'
#Zmienna USE_I18N definiuje, czy aplikacja ma używać międzynarodowych tłumaczeń.
USE_I18N = True
#Zmienna USE_TZ definiuje, czy aplikacja ma używać stref czasowych.
USE_TZ = True
#Zmienna STATIC_URL definiuje URL, pod którym będą dostępne pliki statyczne.
STATIC_URL = '/static/'
#Zmienna STATICFILES_DIRS definiuje katalogi, w których będą szukane pliki statyczne.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
#Zmienna DEFAULT_AUTO_FIELD określa, jakie pole klucza podstawowego ma być używane w modelach.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#Zmienna MEDIA_URL definiuje URL, pod którym będą dostępne pliki multimedialne.
MEDIA_URL = '/media/'
#Zmienna MEDIA_ROOT definiuje katalog, w którym będą przechowywane pliki multimedialne.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#Zmienna CART_SESSION_ID definiuje klucz sesji, który będzie używany do przechowywania koszyka zakupów w sesji użytkownika.
CART_SESSION_ID = 'cart'
#Zmienna os.environ.setdefault definiuje klucz publiczny platformy Stripe, który jest używany do integracji z płatnościami
os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51AROWSJX9HHJ5bycpEUP9dK39tXufyuWogSUdeweyZEXy3LC7M8yc5d9NlQ96fRCVL0BlAu7Nqt4V7N5xZjJnrkp005fDiTMIr')
#Zmienna STRIPE_SECRET_KEY zawiera klucz prywatny platformy Stripe.
STRIPE_SECRET_KEY = 'sk_test_7mJuPfZsBzc3JkrANrFrcDqC'

AUTH_USER_MODEL = 'users.UserBase'
LOGIN_REDIRECT_URL = '/users/dashboard'# gdzie zostaną przekierowani uwierzytelnieni użytkownicy po zalogowaniu
LOGIN_URL = '/users/login/' # gdzie zostan a przekierowani gdy nie są zalogowani
# Zmienna EMAIL_BACKEND określa backend używany do wysyłania wiadomości e-mail. 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

