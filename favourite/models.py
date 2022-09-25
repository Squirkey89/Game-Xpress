from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Favourite(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="FavouriteProduct")

    def __str__(self):
        return str(self.user)


class FavouriteProduct(models.Model):

    products = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
    Favourite = models.ForeignKey(
        Favourite,
        null=False,
        blank=False,
        on_delete=models.CASCADE)
