from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import Coupon



def basket_contents(request):
    coupon_id = request.session.get('discount_id', int())

    basket_items = []
    total = 0
    savings = 0
    coupon_amount = 0
    basket_total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    try:
        coupon = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        coupon = None

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        basket_total += quantity * product.price
        if coupon is not None:
            coupon_amount = coupon.amount
            savings = basket_total*(coupon_amount/Decimal('100'))
            total = basket_total - savings
        else:
            total = basket_total
            
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'coupon': coupon,
        'coupon_amount': coupon_amount,
        'savings': savings,
    }  


    return context


    
