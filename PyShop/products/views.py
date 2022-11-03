from django.shortcuts import HttpResponse, render
from django.http import HttpResponse
# Create your views here.

# we need to tell django to run index when we access /product
# Uniform Resource Locator (Address)


def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')
