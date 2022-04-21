from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from yaml import serialize
from posts.models import Post, LikeDislike
from accounts.models import CustomUser
from .serializers import LikeDislikeSerializer, PostSerializer


class CustomPermission(BasePermission):
    message = "Samo autor može da uređuje objavu."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostPagination(PageNumberPagination):
    page_size = 4


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"
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
        request = serializer.context["request"]
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    def patch(self, request, pk):
        item = self.get_object()
        serializer = self.get_serializer(item)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeAPIView(generics.GenericAPIView):
    serializer_class = LikeDislikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        request = serializer.context["request"]
        post = Post.objects.get(pk=pk)
        is_liked = LikeDislike.objects.get(user=request.user, post=post).value
        if is_liked == 1:
            post.likes -= 1
            post.users_liked.remove(request.user)
            post.save()
        elif is_liked == 0:
            post.likes += 1
            post.users_liked.add(request.user)
            post.save()
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)