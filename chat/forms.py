from .models import Message
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        
        error_messages={
                'body':{
                    'required': 'Popunite ovo polje.'
                },
            }
