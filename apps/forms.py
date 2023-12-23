from django import forms

from apps.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('price', 'image', 'category', 'quantity', 'title')
        # exclude = ('created_at',)

