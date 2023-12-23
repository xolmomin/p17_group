from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import index, add_product, delete_product #, list_post, create_post

urlpatterns = [
    path('', index, name='index'),
    path('add-product', add_product, name='add_product'),
    path('delete-product/<int:pk>', delete_product, name='delete_product'),
    # path('posts-list', list_post, name='index'),
    # path('posts-create', csrf_exempt(create_post), name='index')
]
