from django import forms
from .models import Book


class MarkForm(forms.ModelForm):
    book_id = forms.IntegerField()
    class Meta:
        model = Book
        fields = ['mark',]