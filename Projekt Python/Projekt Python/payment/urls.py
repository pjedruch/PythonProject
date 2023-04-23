from django.urls import path

from . import views

app_name = 'payment'
#adresy URL dla aplikacji Payment, które są przypisane do określonych widoków: CartView, order_placed, Error, i stripe_webhook
urlpatterns = [
    path('', views.CartView, name='cart'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
]