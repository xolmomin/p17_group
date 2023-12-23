from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    user_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return ' '.join(self.title.split()[:4])


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField(blank=True, null=True)
    post = models.ForeignKey('apps.Post', models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/images/', default='products/default.jpg')
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey('apps.Category', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
