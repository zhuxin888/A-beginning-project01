from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    boby = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def _str_(self):
        return self.title
