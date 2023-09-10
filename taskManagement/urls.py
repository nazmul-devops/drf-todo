from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from taskManagement.views.views import *

urlpatterns = [
    path('task/', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend API Task Management APP</h1>", content_type="text/html")),
    path('ping/', HealthCheakAPIView.as_view(), name='ping'),
]