from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Model for posting blog"""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='article_posts')
    description = models.TextField(default="")
    image = models.ImageField(null=True, blank=True)
    body = models.TextField(null=False, blank=True)
    date_published = models.DateTimeField(auto_now=True)
    featured_articles = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Model for comments"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

