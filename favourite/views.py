from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def view_favourite(request):
    """ A view to return the favourite contents page """
    return render(request, 'favourite/favourite.html')
