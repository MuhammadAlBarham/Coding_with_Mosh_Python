from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
from .models import Product
# Create your views here.

# we need to tell django to run index when we access /product
# Uniform Resource Locator (Address)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse('New Products')
