from rest_framework import serializers
from posts.models import Post, LikeDislike
from accounts.models import CustomUser


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('author', "title", "body")


class LikeDislikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.RelatedField(source='post', read_only=True)

    class Meta:
        model = LikeDislike
        fields = ('value')