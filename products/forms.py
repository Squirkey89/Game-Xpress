"""
Forms for product app
"""
from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    To create and edit products by admins.
    """

    class Meta:
        """
        To define the Product model and which fields to exclude.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'


class ReviewForm(forms.ModelForm):
    """
    Form for users to create reviews and ratings for products.
    """
    class Meta:
        """
        To define the Review model and which fields to exclude.
        """
        model = Review
        fields = (
                'title',
                'review',
                'rating',
        )
