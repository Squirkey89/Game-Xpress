from django.contrib import admin
from .models import Favourite, FavouriteProduct

# Register your models here.
admin.site.register(Favourite)
admin.site.register(FavouriteProduct)
