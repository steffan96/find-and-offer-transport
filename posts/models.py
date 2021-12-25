from django.db import models
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from django.urls import reverse
from accounts.models import CustomUser
from django import forms


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
    dislikes = models.SmallIntegerField(default=0)
    users_liked = models.ManyToManyField(CustomUser, related_name='users_liked')
    

    def get_absolute_url_offering(self):
        return reverse('posts:post_detail', args=[str(self.pk)])
    
    #def get_absolute_url_looking(self):
      #  return reverse('looking_new')
    
    def __str__(self):
        return f"{self.author.first_name}: {self.title}"


class LikeDislike(models.Model):
  user = ForeignKey(CustomUser, on_delete=models.CASCADE)
  post = ForeignKey(Post, on_delete=models.CASCADE)
  value = models.SmallIntegerField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user} - {self.value} - {self.post}"
  
  class Meta:
    unique_together = ('user', 'post', 'value')

