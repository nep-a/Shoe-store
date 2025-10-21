from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products

def products(request):
    products = Products.objects.all()
    return render(request, 'product.html', {'products': products})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']
        Products.objects.create(title=title, description=description, price=price, image=image)
        return redirect('product_list')
    return render(request, 'products/product_create.html')

def update(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')
    return render(request, 'products/product_update.html', {'product': product})

def delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_delete.html', {'product': product})
