import datetime

from django.db.models import Count
from django.db.models.functions import TruncDay
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

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


class PostLikeAnalytics(APIView):

    @staticmethod
    def validate_date_param(date_from, date_to):
        try:
            if date_from:
                date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d").date()

            if date_to:
                date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d").date()
        except ValueError:
            return False

        return date_from, date_to

    def get(self, request):
        data = {}
        date_from = request.query_params.get("date_from")
        date_to = request.query_params.get("date_to")

        is_valid = self.validate_date_param(date_from, date_to)

        if not is_valid:
            data["message"] = "You entered an incorrect date format."
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        date_from, date_to = is_valid

        likes = Like.objects.filter(is_active=True)

        if date_from:
            likes = likes.filter(updated_at__gte=date_from)
        if date_to:
            likes = likes.filter(updated_at__lte=date_to)

        likes = (
            likes
            .annotate(date=TruncDay("updated_at"))
            .values("date")
            .annotate(quantity=Count("id"))
            .values("date", "quantity")
        )

        if likes:
            for like in likes:
                date = like["date"].strftime("%Y-%m-%d")
                data[date] = like["quantity"]

            return Response(data, status=status.HTTP_200_OK)

        data["message"] = "No likes for this period."
        return Response(data, status=status.HTTP_404_NOT_FOUND)
