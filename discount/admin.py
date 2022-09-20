from django.contrib import admin
from.models import DiscountCode

# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'active', 'discount']
    search_fields = ['code']


admin.site.register(DiscountCode, DiscountAdmin)
