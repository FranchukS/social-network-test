from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content")
        allow_empty = ("content",)


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "owner", "created_at", "likes_number")


class PostDetailSerializer(serializers.ModelSerializer):
    liked_by = serializers.SlugRelatedField(many=True, slug_field="username", read_only=True,)

    class Meta:
        model = Post
        fields = ("id", "title", "owner", "created_at", "content", "liked_by")


class PostLikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.SlugRelatedField(
        queryset=get_user_model().objects.filter(likes__is_active=True),
        many=True, slug_field="username",
        # read_only=True,
    )

    class Meta:
        model = Post
        fields = ("likes_number", "liked_by")


# class LikeSerializer(serializers.ModelSerializer):
#     liked_by = serializers.SlugRelatedField(many=True, slug_field="username", read_only=True,)
#
#     class Meta:
#         model = Like
#         fields = ("liked_by",)
