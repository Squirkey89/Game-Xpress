from django.shortcuts import render, redirect

# Create your views here.

def view_basket(request):
    """ A view to return the baket contents page """
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('basket', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['basket'] = bag
    return redirect(redirect_url)
