import json
import os
import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings

from cart.cart import Cart
from orders.views import payment_confirmation

#Funkcja "order_placed" usuwa zawartość koszyka (Cart) i wyświetla szablon strony potwierdzenia zamówienia.
def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payment/orderplaced.html')

#Kod definiuje klasę Error dziedziczącą po TemplateView i ustawiającą template_name na 'payment/error.html'.
class Error(TemplateView):
    template_name = 'payment/error.html'

#Funkcja "CartView" zwraca formularz płatności z platformą Stripe, zawierający klienta sekretnego tokena i klucz publiczny, na podstawie danych koszyka oraz autoryzacji użytkownika.
@login_required
def CartView(request):

    cart = Cart(request)
    total = str(cart.get_price_total())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/payment_form.html', {
        'client_secret': intent.client_secret, 
        'STRIPE_PUBLISHABLE_KEY': os.environ.get('STRIPE_PUBLISHABLE_KEY')})

#Funkcja stripe_webhook dekorowana przez csrf_exempt odbiera żądania od bramki płatności Stripe i weryfikuje, czy płatność została pomyślnie zrealizowana, a następnie wywołuje funkcję payment_confirmation lub zwraca odpowiedź HTTP 200.
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)