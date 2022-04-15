from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.pagination import PageNumberPagination
from yaml import serialize
from rest_framework import status
from rest_framework.response import Response
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


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    pagination_class = PostPagination

    def retrieve(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, 
                            status=status.HTTP_201_CREATED)
