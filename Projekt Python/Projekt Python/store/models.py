from django.db import models
from django.urls import reverse
from django.conf import settings


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,verbose_name="Nazwa")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nazwa")
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, verbose_name="Kategoria")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator', verbose_name="Stworzone przez")
    slug = models.SlugField(max_length=255,verbose_name="Slug")
    image = models.ImageField(upload_to='images/', default='images/default.png',verbose_name="Zdjęcie")
    price = models.DecimalField(max_digits=4, decimal_places=2,verbose_name="Cena" )
    description = models.TextField(blank=True,verbose_name="Opis")
    is_active = models.BooleanField(default=True,verbose_name="Aktualny")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Utworzony")
    updated = models.DateTimeField(auto_now=True, verbose_name="Zaktualizowane")
    in_stock = models.BooleanField(default=True, verbose_name="W mgazynie" )

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
