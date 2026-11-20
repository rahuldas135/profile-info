def cart_summary(request):
    cart = request.session.get("shopping_cart", {})
    cart_count = sum(int(value) for value in cart.values() if str(value).isdigit())

    return {
        'cart_count': cart_count,
        'cart': cart
    }
