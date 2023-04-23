from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_quantity)
        cartquantity = cart.__len__()
        response = JsonResponse({'quantity': cartquantity})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cartquantity = cart.__len__()
        carttotal = cart.get_price_total()
        response = JsonResponse({'quantity': cartquantity, 'subtotal': carttotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product=product_id, quantity=product_quantity)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity, 'subtotal': cart.get_price_subtotal(), 'total': cart.get_price_total()})
        return response
