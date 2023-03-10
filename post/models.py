from django.conf import settings
from django.db import models


class BaseBlogModel(models.Model):
    """Base model for with standard field in models"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseBlogModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Like",
        related_name="liked_posts",
    )

    class Meta:
        ordering = ("created_at",)

    @property
    def likes_number(self):
        return self.likes.filter(is_active=True).count()

    def __str__(self):
        return self.title


class Like(BaseBlogModel):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE
    )
