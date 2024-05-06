from django.urls import path

# from aimartians3.products.views import AI_tutorial
from .views import AI_tutorial,Django_tutorial
urlpatterns = [
    path('ai/',AI_tutorial,name="AI_tutorial"),
    path('django/',Django_tutorial,name="Django_tutorial"),
]