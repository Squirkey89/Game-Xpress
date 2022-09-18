"""
Forms for product app
"""
from django import forms
from .models import Review, Product, Category


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
