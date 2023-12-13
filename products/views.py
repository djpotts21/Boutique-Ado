from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all() # Gets all products from the database
    context = {
        'products': products,
    }


    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id) # Gets the product from the database
    context = {
        'product': product,
    }


    return render(request, 'products/product_detail.html', context)