from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .cart import SESSION_CART_KEY, get_cart
from .models import Product


def product_list(request):
    products = Product.objects.filter(is_available=True, stock__gt=0)
    cart = request.session.get(SESSION_CART_KEY, {})
    for product in products:
        product.in_cart = cart.get(str(product.pk), 0)
    return render(request, "store/product_list.html", {"products": products})


def cart_detail(request):
    items, subtotal = get_cart(request)
    return render(request, "store/cart_detail.html", {"items": items, "subtotal": subtotal})


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id, is_available=True)
    cart = request.session.get(SESSION_CART_KEY, {})
    key = str(product.pk)
    quantity = int(cart.get(key, 0))
    if quantity >= product.stock:
        messages.warning(request, f"Only {product.stock} {product.name} available.")
    else:
        cart[key] = quantity + 1
        request.session[SESSION_CART_KEY] = cart
        messages.success(request, f"{product.name} added to your cart.")
    return redirect("store:product_list")


@require_POST
def cart_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get(SESSION_CART_KEY, {})
    try:
        quantity = int(request.POST.get("quantity", "0"))
    except ValueError:
        quantity = 0
    if quantity <= 0 or not product.is_available:
        cart.pop(str(product.pk), None)
        messages.info(request, f"{product.name} removed from your cart.")
    else:
        cart[str(product.pk)] = min(quantity, product.stock)
        messages.success(request, "Cart updated.")
    request.session[SESSION_CART_KEY] = cart
    return redirect("store:cart_detail")


@require_POST
def cart_remove(request, product_id):
    cart = request.session.get(SESSION_CART_KEY, {})
    cart.pop(str(product_id), None)
    request.session[SESSION_CART_KEY] = cart
    messages.info(request, "Item removed from your cart.")
    return redirect("store:cart_detail")
