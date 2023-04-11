from django import forms
from .models import BookReview


class CreateBookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['book', 'user', 'text', ]


class UpdateBookReviewForm(forms.ModelForm):
    review_id = forms.IntegerField()
    user_id = forms.IntegerField()
    class Meta:
        model = BookReview
        fields = ['text', ]
