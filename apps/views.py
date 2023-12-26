from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.forms import ProductForm, RegisterForm
from apps.models import Post, Product, Category


def index(request):
    context = {
        'products': Product.objects.order_by('-price', 'id')
    }
    return render(request, 'apps/product/product_list.html', context)


#
# def add_product(request):
#     if request.method == 'POST':
#         Product.objects.create(
#             title=request.POST['title'],
#             price=request.POST['price'],
#             category_id=request.POST['category'],
#             image=request.FILES['image'],
#             quantity=request.POST['quantity']
#         )
#         return redirect('index')
#     return render(request, 'apps/product/product_add.html')


# with form
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, files=request.FILES)
        form.is_valid()
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'apps/product/product_add_with_form.html', context)


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect('index')


def register_page(request):
    form = RegisterForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'apps/profile/register.html', context)

    return render(request, 'apps/profile/register.html', context)


def main_page(request):
    return render(request, 'apps/profile/main.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('main_page')

    return render(request, 'apps/profile/login.html')


def form_page(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'apps/forms.html', context)
