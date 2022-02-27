from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.pagination import PageNumberPagination
from posts.models import Post
from .serializers import PostSerializer


class PostUserWritePermission(BasePermission):
    message = 'Samo autor može da uređuje objavu.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostPagination(PageNumberPagination):
    page_size = 4


class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.all_objects.all()
    lookup_field = 'pk'
    pagination_class = PostPagination
    

    def get_queryset(self):
        return Post.objects.all().order_by('-created')


