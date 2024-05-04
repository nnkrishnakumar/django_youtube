from django.urls import path
from aim_tutorial.views import hello
urlpatterns = [
    path("home/",hello,name="home_page")
]
