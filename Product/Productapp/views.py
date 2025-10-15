from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def userDetails(request):
    product = Product.object.all()
    return render(request,'user.html',{'product':product})