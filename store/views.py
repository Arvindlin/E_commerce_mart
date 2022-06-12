from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    """View to get/Retrive the data from the database."""
    product = Product.objects.all()
    return render(request, 'store/home.html', {'product': product})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/details.html', {'product': product})