from django.db import models


class Post(models.Model):
    user_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
