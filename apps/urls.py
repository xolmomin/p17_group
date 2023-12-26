from django.urls import path

from .views import index, add_product,login_page,logout_page, main_page, register_page, delete_product, form_page  # , list_post, create_post


urlpatterns = [
    path('', index, name='index'),
    path('add-product', add_product, name='add_product'),
    path('login', login_page, name='login_page'),
    path('logout', logout_page, name='logout_page'),
    path('main', main_page, name='main_page'),
    path('register', register_page, name='register'),
    path('delete-product/<int:pk>', delete_product, name='delete_product'),
    path('form', form_page, name='form_page'),
    # path('posts-list', list_post, name='index'),
    # path('posts-create', csrf_exempt(create_post), name='index')
]
