# from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from apps.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'apps/index.html', context)

#
# from apps.models import Post
#
#
# def index(request):
#     d = {
#         'key': 'value'
#     }
#     return JsonResponse(d, status=203)
#
#
# def list_post(request):
#     posts = Post.objects.all()  # select * from apps_post;
#     return JsonResponse(posts)
#
#
# def create_post(request):
#     user_id = request.POST.get('userId')
#     title = request.POST.get('title')
#     body = request.POST.get('body')
#     Post.objects.create(user_id=user_id, title=title, body=body)  # insert into apps_post values(1,2,3,4);
#     return JsonResponse({"status": "Created!"}, status=201)
#
#
# ''''
# {
#     "userId": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }
#
#
# '''
# # localhost:8000/main
