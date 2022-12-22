from django.db import models

import blog.settings


class BaseBlogModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Post(BaseBlogModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(
        blog.settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE
    )
    liked_by = models.ManyToManyField(
        blog.settings.AUTH_USER_MODEL,
        through="Like",
        related_name="liked_posts",
    )

    class Meta:
        ordering = ("created_at",)


class Like(BaseBlogModel):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(
        blog.settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE
    )