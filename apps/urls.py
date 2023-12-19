from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index #, list_post, create_post

urlpatterns = [
    path('main', index, name='index'),
    # path('posts-list', list_post, name='index'),
    # path('posts-create', csrf_exempt(create_post), name='index')
]

