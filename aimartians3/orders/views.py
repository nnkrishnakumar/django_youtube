from django.shortcuts import render
from django.http import HttpResponse

def ai_order(request):
    return HttpResponse("Artificial intelligence order has been placed.")

def django_order(request):
    return HttpResponse("Django tutorial order has been placed.")