from django.urls import path
from .views import order
urlpatterns=[
    path('order/',order,name="order_urls")
]