from django import forms
from .models import *


class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ['title', 'desc', 'user', ]


class RelationshipForm(forms.ModelForm):
    class Meta:
        model = BookWishListRelationship
        fields = ['wish_list', 'book',]
