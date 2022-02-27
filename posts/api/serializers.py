from rest_framework import serializers
from posts.models import Post
from accounts.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'looking', 'offering', 'slug')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email','first_name', 'last_name', 'is_active']


