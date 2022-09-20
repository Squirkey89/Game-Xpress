from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class DiscountCode(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField(default=1,
                                   validators=
                                   [MaxValueValidator(100),
                                    MinValueValidator(1)])
    active = models.BooleanField()

    def __str__(self):
        return self.code