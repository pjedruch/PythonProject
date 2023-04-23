from django.shortcuts import get_object_or_404, render

from .models import Category, Product

#Funkcja zwracająca stronę główną sklepu internetowego wraz z listą kategorii i produktów podzielonych na kategorie.
def products_all(request):
    categoriesObjects = Category.objects.all()
    categories = []
    for category in categoriesObjects:
        products = Product.products.filter(category = category)
        categories.append({
            'category': category,
            'products': products,
        })
    
    return render(request, 'store/index.html', {'products': products, 'categories': categories})
# Funkcja "category_list" zwraca widok listy produktów przypisanych do określonej kategorii, 
# pobierając kategorię na podstawie jej sluga z żądania, a następnie filtrowując produkty z kategorią równą wybranej.
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})

# zwraca szablon z widokiem pojedynczego produktu na podstawie podanego sluga, 
# a jeśli produkt o podanym slugu nie istnieje lub nie jest dostępny w magazynie, zwraca stronę błędu 404.
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})
