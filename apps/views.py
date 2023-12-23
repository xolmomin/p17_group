from django.shortcuts import render, redirect

from apps.forms import ProductForm
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
