from rest_framework import serializers

import blog.settings
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
    class Meta:
        model = Post
        fields = ("id", "title", "owner", "created_at", "content", "liked_by")


class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.SlugRelatedField(blog.settings.AUTH_USER_MODEL.username)

    class Meta:
        model = Like
        fields = ("liked_by",)
