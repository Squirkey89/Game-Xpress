from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import Coupon

from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view to return the basket contents page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a product to the shopping basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {basket[item_id]}'
            )
    else:
        basket[item_id] = quantity
        messages.success(
            request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust uantity of the product to the basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a product to the shopping basket """
    product = get_object_or_404(Product, pk=item_id)

    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@require_http_methods(["GET", "POST"])
def add_coupon(request):
    code = request.POST.get('coupon-code')

    if not code:
        messages.error(request, "You didn't enter a coupon code!")
        return redirect(reverse('view_basket'))

    try:
        coupon = Coupon.objects.get(code=code)
        request.session['coupon_id'] = coupon.id
        messages.success(request, f'Coupon code: { code } has been applied')
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        messages.warning(request, f'Coupon code: { code } not accepted')
        return redirect('view_basket')
    else:
        return redirect('view_basket')
