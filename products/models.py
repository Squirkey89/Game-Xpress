from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(
        max_length=254, null=True, blank=True
        )
    name = models.CharField(max_length=254)
    description = models.TextField()
    genre = models.CharField(
        max_length=254, blank=True, default=True
        )
    price = models.DecimalField(
        max_digits=6, decimal_places=2
        )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True
        )
    image = models.ImageField(
        null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(
        verbose_name=('Review Title'),
        max_length=25,
        null=False,
        blank=False
        )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    review = models.TextField(null=True,
                              blank=False
                              )
    rating = models.IntegerField(default=0, validators=[
                    MinValueValidator(1),
                    MaxValueValidator(5)])

    def __str__(self):
        return self.review
