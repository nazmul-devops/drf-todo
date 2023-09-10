from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend API Core APP</h1>", content_type="text/html")),
]