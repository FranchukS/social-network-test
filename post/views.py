from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Override destroy method to make post get inactive,
        instead of be deleted"""

        post = self.get_object()
        post.is_active = False
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
