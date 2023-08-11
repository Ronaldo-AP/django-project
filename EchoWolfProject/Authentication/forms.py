import re

from django import forms

# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .toastMessages import ToastMessagesModel
from .models import User

class LoginForm (AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = username.lower()
        return username
    

class SignUpForm (forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = username.lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(ToastMessagesModel.usernameAlreadyExist())
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(ToastMessagesModel.emailAlreadyExist())
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if password and not re.match(r'^[A-Za-z0-9@#$%^&+=\.]{8,}$', password):
            raise forms.ValidationError(ToastMessagesModel.passNotValid())
        
        return password