from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from post.models import Post, Like
from post.serializers import (
    PostSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostLikeSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        if self.action == "like":
            return PostLikeSerializer

        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Override destroy method to make post get inactive,
        instead of be deleted"""

        post = self.get_object()
        post.is_active = False
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["POST"],
        detail=True,
        url_path="like",
    )
    def like(self, request, pk=None):
        """Endpoint for like/unlike specific post by user"""
        user = self.request.user
        post = self.get_object()
        serializer = self.get_serializer(post)

        # check if user already liked post
        if user in post.liked_by.all():
            like = post.likes.get(user=self.request.user)
            like.is_active = not like.is_active
            like.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        Like.objects.create(post=post, user=user)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
