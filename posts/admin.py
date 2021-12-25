from django.contrib import admin

from .models import Post, LikeDislike

admin.site.register(Post)
admin.site.register(LikeDislike)
