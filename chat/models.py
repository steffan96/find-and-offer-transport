import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.utils.text import slugify
from accounts.models import CustomUser


class ChatBox(models.Model):
    user1  = models.ForeignKey(CustomUser, 
    on_delete=models.CASCADE, related_name='user1')
    user2  = models.ForeignKey(CustomUser, 
    on_delete=models.CASCADE, related_name='user2')
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
      if not self.slug:
        random_slug = uuid.uuid4()
        self.slug = slugify(random_slug)
      super(ChatBox, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user1.first_name} {self.user1.last_name} \
        and {self.user2.first_name} {self.user2.last_name} chat"


class Message(models.Model):
  chat = models.ForeignKey(ChatBox, on_delete=models.CASCADE, related_name='related_chat')
  sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  seen = models.BooleanField(default=False)
  
  class Meta:
        ordering = ['-created']

  def __str__(self):
      return f"{self.chat}: message nr: {self.pk}"
