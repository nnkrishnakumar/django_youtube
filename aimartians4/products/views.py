from django.shortcuts import render

def products(request):
    return render(request,'products.html')

def home(request):
    return render(request,'home.html')