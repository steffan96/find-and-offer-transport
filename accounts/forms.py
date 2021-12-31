from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.base import Model
from django.forms import widgets
from django.forms.models import ModelForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'city', 'country',)
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'city': 'Grad',
            'country': 'Država',
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
        fields = ('first_name', 'last_name', 'email', 'city', 'country',)
        exclude = ('password', 'image', 'email')
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'city': 'Grad',
            'country': 'Država',
        }

    