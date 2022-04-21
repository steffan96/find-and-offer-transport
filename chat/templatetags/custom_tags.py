from django import template
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from accounts.models import CustomUser
from chat.models import ChatBox, Message

register = template.Library()


@register.simple_tag(name="unseen_count")
def unseen_count(receiver_pk, obj_pk):
    user = CustomUser.objects.get(id=receiver_pk)
    chat1 = ChatBox.objects.get(id=obj_pk)
    return Message.objects.filter(receiver=user, seen=False, chat=chat1).count()
