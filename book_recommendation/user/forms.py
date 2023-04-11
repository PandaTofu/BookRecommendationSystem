from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms

from .models import User


class UserSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'gender']


class UpdatePasswordForm(PasswordChangeForm):
    user_id = forms.IntegerField()


class UserProfileGetForm(forms.Form):
    user_id = forms.IntegerField()


class UserProfileUpdateForm(UserChangeForm):
    user_id = forms.IntegerField()
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['id', 'email', 'gender']