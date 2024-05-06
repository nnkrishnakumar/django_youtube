from django.shortcuts import render
from django.http import HttpResponse

def AI_tutorial(request):
    return HttpResponse("Artificial Intelligence Tutorial is available")

def Django_tutorial(request):
    return HttpResponse("Django Tutorial is available")
