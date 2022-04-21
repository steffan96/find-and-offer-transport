from rest_framework import serializers
from posts.models import Post
from accounts.models import CustomUser


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('author', "title", "body")

    # def save(self, **kwargs):
    #     user = self.context['request'].user