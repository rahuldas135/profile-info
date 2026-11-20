from decimal import Decimal

from .models import Product


SESSION_CART_KEY = "shopping_cart"


def get_cart(request):
    """Return cart rows and a Decimal subtotal, trimming stale or excess items."""
    cart = request.session.get(SESSION_CART_KEY, {})
    if not isinstance(cart, dict):
        cart = {}

    products = Product.objects.filter(
        id__in=[key for key in cart if str(key).isdigit()], is_available=True
    )
    items = []
    subtotal = Decimal("0.00")
    normalized = {}

    for product in products:
        try:
            quantity = int(cart.get(str(product.pk), 0))
        except (TypeError, ValueError):
            continue
        quantity = min(max(quantity, 0), product.stock)
        if quantity == 0:
            continue
        line_total = product.price * quantity
        items.append({"product": product, "quantity": quantity, "line_total": line_total})
        normalized[str(product.pk)] = quantity
        subtotal += line_total

    if normalized != cart:
        request.session[SESSION_CART_KEY] = normalized
    return items, subtotal
