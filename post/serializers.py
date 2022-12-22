from rest_framework import serializers

from post.models import Post, Like


class ActiveLikeSerializer(serializers.ListSerializer):
    """ Filter so only active likes are shown """
    def to_representation(self, data):
        data = data.filter(is_active=True)
        return super(ActiveLikeSerializer, self).to_representation(data)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        list_serializer_class = ActiveLikeSerializer
        fields = ("user",)


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
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id", "title", "owner", "created_at", "content", "likes")


class PostLikeSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True)

    class Meta:
        model = Post
        fields = ("likes_number", "likes")
