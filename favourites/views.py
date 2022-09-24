from django.shortcuts import render


def view_favourites(request):
    """ A view to return the favourite contents page """
    return render(request, 'favourites/favourites.html')
