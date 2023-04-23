from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)

app_name = 'users'
#To zestaw adresów URL dla aplikacji internetowej zawierający m.in. widoki logowania, wylogowywania, rejestracji użytkownika, resetowania hasła, profilu użytkownika oraz panelu użytkownika.
urlpatterns = [
    path(
          'login/',
          auth_views.LoginView.as_view(template_name='users/login.html', form_class=UserLoginForm),
          name='login'
     ),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name='logout'),
    path('register/', views.users_register, name='register'),
    path('activate/<uidb64>/<token>)/', views.users_activate, name='activate'),
    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset/password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='users/password_reset/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset/password_reset_confirm.html',
                                                                                                success_url='password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="users/password_reset/reset_status.html"), name='password_reset_done'),
    path('password_reset_confirm/Nw/password_reset_complete/',
         TemplateView.as_view(template_name="users/password_reset/reset_status.html"), name='password_reset_complete'),
    # User dashboard
    path('profile/delete_confirm/', TemplateView.as_view(template_name="users/dashboard/delete_confirm.html"), name='delete_confirmation'),
    path('profile/delete_user/', views.delete_user, name='delete_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),
]
