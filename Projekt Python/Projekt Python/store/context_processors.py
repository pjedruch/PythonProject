from .models import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }
#funkcja zwraca słownik, w którym kluczem jest 'categories', a wartością jest lista wszystkich obiektów Category w bazie danych.