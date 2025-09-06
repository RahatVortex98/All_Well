# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from landingPage.models import Products

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        cart[str(product_id)]["quantity"] += 1
    else:
        cart[str(product_id)] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
            "image": product.image.url if product.image else "",
        }

    request.session["cart"] = cart
    return redirect("cart_view")

def cart_view(request):
    cart = request.session.get("cart", {})
    total = 0
    for item in cart.values():
        item["line_total"] = item["price"] * item["quantity"]
        total += item["line_total"]

    return render(request, "cart.html", {"cart": cart, "total": total})


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session["cart"] = cart
        messages.success(request, "Item removed from cart.")

    return redirect("cart_view")
