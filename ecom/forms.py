from django import forms
from .models import Products


class ItemForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_category',
                  'product_description', 'product_image']
