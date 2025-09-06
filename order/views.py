# orders/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import CheckoutForm
from landingPage.models import Products

def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        return redirect("cart_view")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data["payment_method"]

            # calculate total
            total = sum(item["price"] * item["quantity"] for item in cart.values())

            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                payment_method=payment_method,
                total=total,
                is_paid=(payment_method == "COD"),  # COD -> mark paid on delivery
            )

            # Save items
            for product_id, item in cart.items():
                product = Products.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                    price=item["price"],
                )

            # Clear cart
            request.session["cart"] = {}

            # If bKash → redirect to bKash API flow
            if payment_method == "BKASH":
                return redirect("bkash_payment", order_id=order.id)

            return render(request, "order_success.html", {"order": order})
    else:
        form = CheckoutForm()

    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return render(request, "checkout.html", {"form": form, "cart": cart, "total": total})




def bkash_payment(request, order_id):
    # Later you will integrate bKash API here
    return render(request, "bkash_payment.html", {"order_id": order_id})


def order_success(request):
    return render(request, "order_success.html")
