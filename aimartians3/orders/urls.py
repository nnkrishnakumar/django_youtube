from django.urls import path
from .views import ai_order,django_order

urlpatterns = [
    path('ai_order/',ai_order,name="AI_tutorial"),
    path('django_order/',django_order,name="Django_tutorial"),
]