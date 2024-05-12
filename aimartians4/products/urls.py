from django.urls import path
from .views import products,home
urlpatterns=[
    path('prod/',products, name="aimartians products"),
    path('home/',home)
]