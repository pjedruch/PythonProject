from django.contrib import admin

from .models import Order, OrderItem

admin.site.register(OrderItem)
#W klasie OrderAdmin definiowane są atrybuty, które definiują sposób wyświetlania i filtrowania obiektów Order w panelu administracyjnym.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'full_name', 'payment_type', 'total_paid', 'billing_status', 'is_done']
    list_filter = ['user', 'is_done']
    list_editable = ['is_done', 'billing_status']
