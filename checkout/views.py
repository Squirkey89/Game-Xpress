from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm



# Create your views here.
def checkout(request):
    """
    To process checkout
    """
    
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51LPUbhLloG8FpSifQgdhA2G5fBsWvxSR96UsffWt8BGZjPnArOuJUfJrWktP7FRbdZR8nlOIQ6lg1c8rC57Ylbhu00Bkkv3oJl",
        'client_secret': "test_client_secret",
    }

    return render(request, template, context)
