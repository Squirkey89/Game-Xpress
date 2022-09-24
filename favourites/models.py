from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Favourites(models.Model):
    """
    A model that keeps track of users favourite items.
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,blank=True)