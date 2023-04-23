from django.urls import path

from . import views

app_name = 'orders'
# kod definiuje pojedynczą ścieżkę URL dla aplikacji "orders", która wywołuje widok "add" w module "views"
urlpatterns = [
    path('add/', views.add, name='add'),
]