from rest_framework import serializers
from django.shortcuts import get_object_or_404  
from posts.models import Post, LikeDislike, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = ("author", "title", "body",)


class LikeDislikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    
    class Meta:
        model = LikeDislike
        fields = (
            "user",
            "post",
        )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "body",
            "user",
            "post",
        )
