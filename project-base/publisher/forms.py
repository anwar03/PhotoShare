from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class signUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email","username", "password1", "password2")


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')