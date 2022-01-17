import random
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.forms import widgets
from django.forms.models import ModelForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'city')
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'city': 'Grad',
            #'country': 'Država',
        }
        error_messages={
                'password_mismatch':{
                    _('Šifre se ne podudaraju'),
                },
                'body':{
                    'required': 'Popunite ovo polje.'
                },
            }


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'city',)
        exclude = ('username', 'password', 'image', 'email')
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'city': 'Grad',
            
        }

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user
