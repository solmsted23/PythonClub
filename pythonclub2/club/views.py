from django.shortcuts import render, get_object_or_404
from .models import Product, TechType, Review
# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def products(request):
    product_list=Product.all()
    return render(request), 'club/products.html', {'product_list': product_list}

def productDetail(request, id):
    product=get_object_or_404(Product, pk=id)
    return render(request, 'club/productdetail.html', {'product' : product})
