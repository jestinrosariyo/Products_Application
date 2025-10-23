from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request,'index.html')

def userDetails(request):
    product = Product.objects.all()
    return render(request,'user.html',{'product':product})

def typeShow(request):
    types = Product.objects.values_list('type', flat=True).distinct()
    return render (request,'type.html',{'types': types})

def getDetails(request,types):
    details = Product.objects.filter(type=types)
    return render(request, 'user.html', {'details': details})