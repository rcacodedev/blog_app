"""
Forms for the accounts app.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    """
    Form for registering a new user.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    country = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'username',  'country']

