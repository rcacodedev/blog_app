"""
Model definitions for the blog_app app.
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """ Model definition for the Category model. """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """ Model definition for the Tag model. """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ Model definition for the Post model. """
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """ Model definition for the Comment model. """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

