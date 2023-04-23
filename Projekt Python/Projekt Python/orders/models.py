from decimal import Decimal
from django.conf import settings
from django.db import models

from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user', verbose_name="Użytkownik")
    full_name = models.CharField(max_length=50, verbose_name="Imię i nazwisko")
    address1 = models.CharField(max_length=250, verbose_name="Ulica i numer domu")
    address2 = models.CharField(max_length=250, verbose_name="Miasto")
    phone = models.CharField(max_length=100, verbose_name="Telefon")
    post_code = models.CharField(max_length=20, verbose_name="Kod pocztowy")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Utworzone")
    updated = models.DateTimeField(auto_now=True, verbose_name="Zaktualizowany")
    total_paid = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cena zamówienia")
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=True, verbose_name="Status płatności")

    is_done = models.BooleanField(verbose_name='Wykonane', default=False)

    payment_type = models.CharField(
        max_length=24,
        choices=[('card', 'Karta płatnicza'), ('cash', 'Gotówka')],
        verbose_name='Sposób płatności',
        default='card'
    )

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
#Ten kod definiuje dwa modele Django: Order i OrderItem, 
# które reprezentują zamówienia oraz ich pozycje w sklepie internetowym. Model Order zawiera informacje o użytkowniku, 
# cenie zamówienia, statusie płatności i sposobie płatności, a także adresie dostawy. Model OrderItem reprezentuje 
# pojedynczą pozycję w zamówieniu, zawiera informacje o produkcie, cenie i ilości. Oba modele mają relacje między sobą, 
# a także z modelem Product zdefiniowanym w innym module.