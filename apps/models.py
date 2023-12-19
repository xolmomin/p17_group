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



'''
1,2,3
photos -> csv
albums -> csv

django adminka

15:40
30min


import csv






1.
dunderMethod -> dunder_method

'''

