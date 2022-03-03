import random
from django.contrib.auth.forms import UserCreationForm

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
                    _('Lozinke se ne podudaraju'),
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

    

