from random import random
import uuid
from django.db import models
from django.db.models.fields import BooleanField, related
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from accounts.models import CustomUser
from django import forms


class SoftDeleteManager(models.Manager):
  def get_queryset(self):
      return super().get_queryset().filter(is_deleted=False)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=650)
    author  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
    null=True, blank=True, related_name='author')
    looking = models.BooleanField(default=False)
    offering = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.SmallIntegerField(default=0)
    users_liked = models.ManyToManyField(CustomUser, related_name='users_liked', blank=True)
    is_deleted = models.BooleanField(default=False)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)

    def save(self, *args, **kwargs):
      if not self.slug:
        random_slug = uuid.uuid4()
        self.slug = slugify(random_slug)
      super(Post, self).save(*args, **kwargs)

    def get_absolute_url_offering(self):
        return reverse('posts:post_detail', args=[str(self.pk)])
    
    def soft_delete(self):
      self.is_deleted = True
      self.save()
    
    def restore(self):
      self.is_deleted = False
      self.save()

    def __str__(self):
        return f"{self.author.first_name}: {self.title}"
    
    objects = SoftDeleteManager()
    all_objects = models.Manager()

class LikeDislike(models.Model):
  user = ForeignKey(CustomUser, on_delete=models.CASCADE)
  post = ForeignKey(Post, on_delete=models.CASCADE)
  value = models.SmallIntegerField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user} - {self.value} - {self.post}"
  
  class Meta:
    unique_together = ('user', 'post', 'value')


class Comment(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.body[:40])


