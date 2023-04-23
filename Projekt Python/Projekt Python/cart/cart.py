from decimal import Decimal

from django.conf import settings

from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}

        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
        self.save()

    def get_price_subtotal(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_price_total(self):

        subtotal = self.get_price_subtotal()

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(5)

        total = subtotal + Decimal(shipping)
        return total

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True