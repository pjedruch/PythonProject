from django.http.response import JsonResponse
from django.shortcuts import render

from cart.cart import Cart

from .models import Order, OrderItem

#add(request) tworzy obiekt Order i przypisuje mu obiekty OrderItem, na podstawie wprowadzonych przez użytkownika danych i zawartości koszyka.
def add(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_key = request.POST.get('order_key')
        full_name = request.POST.get('full_name')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        post_code = request.POST.get('post_code')
        phone = request.POST.get('phone')
        payment_type = request.POST.get('payment_type')

        user_id = request.user.id
        carttotal = cart.get_price_total()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name=full_name,
                address1=address1,
                address2=address2,
                post_code=post_code,
                payment_type=payment_type,
                phone=phone,
                total_paid=carttotal,
                order_key=order_key
            )
            order_id = order.pk

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['quantity'])

        response = JsonResponse({'success': 'Return something'})
        return response

#payment_confirmation(data) aktualizuje status płatności obiektu Order o podanym kluczu zamówienia.
def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

#user_orders(request) pobiera wszystkie obiekty Order powiązane z aktualnie uwierzytelnionym użytkownikiem.
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    return orders
