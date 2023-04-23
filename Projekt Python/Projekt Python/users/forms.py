from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import UserBase

# Kod definiuje klasę formularza logowania użytkownika dziedziczącą po klasie AuthenticationForm 
# z modułu django.contrib.auth.forms, która zawiera pola 'username' i 'password' z odpowiednimi 
# atrybutami widgetów formularza.
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Hasło',
            'id': 'login-pwd',
        }
    ))

# Klasa RegistrationForm dziedziczy po forms.ModelForm i definiuje 
# formularz rejestracji użytkownika, który wymaga podania nazwy użytkownika, 
# adresu email oraz dwukrotnego wprowadzenia hasła, a następnie weryfikuje 
# poprawność wprowadzonych danych i uaktualnia pola formularza o odpowiednie atrybuty CSS.
class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Nazwa Użytkownika', min_length=4, max_length=50, help_text='Wymgane')
    email = forms.EmailField(max_length=100, help_text='Wymgane', error_messages={
        'Wymgane': 'Proszę wprowadzić adres email'})
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Nazwa użytkownika już istnieje")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są zgodne.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Użyj innego adresu e-mail, wprowadzony adres jest już zajęty')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nazwa użytkownika'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Hasło'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Powtórz hasło'})

# Klasa PwdResetForm dziedziczy po klasie PasswordResetForm i definiuje pole formularza email, 
# które pozwala na wprowadzenie adresu e-mail użytkownika, któremu ma zostać wysłany link do zresetowania hasła. 
class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Niestety nie możemy znaleźć tego adresu e-mail.')
        return email

# Klasa PwdResetConfirmForm tworzy formularz zmiany hasła z dwoma polami wprowadzania hasła i 
# odpowiadającymi im etykietami i atrybutami.
class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Nowe hasło', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nowe hasło', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Powtórz hasło', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Powtórz hasło', 'id': 'form-new-pass2'}))

# Klasa UserEditForm reprezentuje formularz edycji danych użytkownika, 
# który zawiera pola umożliwiające edycję imienia i e-maila, 
# przy czym pole e-mail jest tylko do odczytu
class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-mail konta (nie mona zmienić)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'e-mail', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Imię', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nazwa użytkownika', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Nazwa użytkownika', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Imię', 'id': 'form-lastname'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True