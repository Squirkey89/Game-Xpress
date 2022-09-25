from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Favourite

# Create your views here.

@login_required
def view_favourite(request):
    """ A view to return the favourite contents page """

    favourite = None
    try:
        favourite = Favourite.objects.get(user=request.user)
    except Favourite.DoesNotExist:
        pass

    context = {
        'favourite': favourite,
    }

    return render(request, 'favourite/favourite.html', context)


@login_required
def add_to_favourite(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    favourites, _ = Favourite.objects.get_or_create(user=request.user)

    favourites.products.add(product)
    messages.info(request, f'{product.name} was added to your favourites')

    return redirect(redirect_url)