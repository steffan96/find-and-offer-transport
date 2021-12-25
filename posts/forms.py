from django.db.models import fields
from django.forms import ModelForm
from .models import Post, Comment
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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
        error_messages={
                'body':{
                    'required': 'Popunite ovo polje.'
                },
            }