from django.forms import ModelForm

from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ("body",)

        error_messages = {
            "body": {"required": "Popunite ovo polje."},
        }
