from rest_framework import serializers
from posts.models import Post
from accounts.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')


