from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

# klasa służy do generowania tokenów aktywacyjnych użytkowników na podstawie klucza głównego, znacznika czasu oraz informacji o stanie aktywności użytkownika
class UsersActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )


users_activation_token = UsersActivationTokenGenerator()