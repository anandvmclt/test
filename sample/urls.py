# Sample/urls.py

from django.urls import path, include
from .views import index, Home
app_name = "sample"

urlpatterns = [
    path('', index, name="index"),
    path('home', Home.as_view(), name="home")
]
