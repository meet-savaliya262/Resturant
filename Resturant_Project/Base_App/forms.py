from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
