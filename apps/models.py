from django.db import models


class Post(models.Model):
    user_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return ' '.join(self.title.split()[:4])

    # class Meta:
    #     verbose_name = 'Elon'
    #     verbose_name_plural = 'Elonlar'


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField(blank=True, null=True)
    post = models.ForeignKey('apps.Post', models.CASCADE)
    # thumbnailUrl
    # thumbnail_url


'''
POST

{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  
COMMENT
 {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  }

'''
