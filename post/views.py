from rest_framework import viewsets

from post.models import Post
from post.serializers import (
    PostSerializer,
    PostListSerializer,
    PostDetailSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        return PostSerializer
