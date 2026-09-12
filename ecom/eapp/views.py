from django.shortcuts import render
from .models import Product
# Create your views here.

def cart(request):
    return render(request,'cart.html')

def home(request):
    pr=Product.objects.all()
    return render(request,'index.html',{'pr':pr})

def login(request):
    return render(request,'login.html')

def sign(request):
    return render(request,'signup.html')

def check(request):
    return render(request,'check.html')