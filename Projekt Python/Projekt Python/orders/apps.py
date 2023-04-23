from django.apps import AppConfig

# AppConfig to klasa bazowa dla konfiguracji aplikacji Django, która służy do skonfigurowania aplikacji "orders".
class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
