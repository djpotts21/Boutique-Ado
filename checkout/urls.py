from django.urls import path
from . import views
from .webhooks import webhook
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', csrf_exempt(webhook), name='webhook'),
]
