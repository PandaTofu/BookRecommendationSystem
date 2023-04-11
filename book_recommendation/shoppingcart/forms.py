from django import forms
from .models import ShoppingCartItem


class ShoppingCartItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['book', 'user',]
