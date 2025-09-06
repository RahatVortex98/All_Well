from django.urls import path
from .views import checkout,order_success,bkash_payment

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("success/", order_success, name="order_success"),
    path("bkash/<int:order_id>/", bkash_payment, name="bkash_payment"),
]
