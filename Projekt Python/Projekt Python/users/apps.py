from django.apps import AppConfig

#definiuje konfigurację aplikacji "users" w Django, ustawiając domyślne pole klucza głównego na BigAutoField.
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
