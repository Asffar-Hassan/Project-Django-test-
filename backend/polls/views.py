from django.shortcuts import render
from .models import Categories,Gamme,Product

# Create your views here.

def index(request):
    products=Product.objects.all()
    list_prod={
        'products':products
    }

    return render(request,'index-shop.html',list_prod)

def about(request):
    return render(request,'about.html')
