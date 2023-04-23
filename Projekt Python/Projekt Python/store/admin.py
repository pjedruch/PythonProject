from django.contrib import admin

from .models import Category, Product

#Kod rejestruje model Category w panelu administracyjnym Django, 
# określa jakie pola modelu mają być wyświetlane w liście obiektów i ustawia automatyczne wypełnianie pola "slug" na podstawie pola "name".
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price',
                    'in_stock', 'created', 'updated', 'slug']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
# definiuje klasę ProductAdmin, która dziedziczy po klasie ModelAdmin z modułu admin Django i 
# rejestruje model Product jako element panelu administracyjnego z włączonymi funkcjami takimi 
# jak filtrowanie i edycja listy produktów, wyświetlanie ich atrybutów i automatyczne wypełnianie pola slug.