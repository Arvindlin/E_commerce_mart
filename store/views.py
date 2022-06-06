from django.shortcuts import render
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    """View to get/Retrive the data from the database."""
    product = Product.objects.all()
    return render(request, 'store/home.html', {'products': product})