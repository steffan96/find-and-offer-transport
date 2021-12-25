from django.db.models import fields
from django.forms import ModelForm
from .models import Post
from django import forms


class OfferingCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        error_messages={
                'title':{
                    'required': 'Popunite ovo polje.'
                },
                'body':{
                    'required': 'Popunite ovo polje.'
                },
            }
