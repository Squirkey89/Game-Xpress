from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'description',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """
    Category admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewsAdmin(admin.ModelAdmin):

    readonly_fields = ('added_by', )

    list_display = (
        'review',
        'user',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewsAdmin)
