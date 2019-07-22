from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products =Product.objects.all()
    return render(request,"index.html", {"products" : products})


def new(request):
    return HttpResponse("mis cojones nuevos")


def inicio(request):
    return render(request,"inicio.html")


def detail(request,product_id):
    products = Product.objects.get(id=product_id)
    return render(request, "detail.html", {"products": products})
