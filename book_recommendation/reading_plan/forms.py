from django import forms
from .models import ReadingPlan


class ReadingPlanForm(forms.ModelForm):
    class Meta:
        model = ReadingPlan
        fields = ['user', 'book_name', 'period_days', 'pages_per_day']
