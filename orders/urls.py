from django.urls import path 
from .views import add_to_cart,order_list,checkout,process_payment,payment_success,payment_failed

urlpatterns = [
    path('' , order_list),
    path('checkout/' , checkout),
    path('checkout/process-payment' , process_payment),
    path('checkout/payment/success' , payment_success),
    path('checkout/payment/failed' , payment_failed),
    
    path('add-to-cart', add_to_cart),
]
