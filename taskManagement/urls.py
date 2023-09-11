from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from taskManagement.views.views import *
from taskManagement.views.func_base_views import *
from taskManagement.models.models import *

urlpatterns = [
    path(
        "",
        lambda request: HttpResponse(
            "<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend API Task Management APP</h1>",
            content_type="text/html",
        ),
    ),
    path("ping/", HealthCheakAPIView.as_view(), name="ping"),
    path("project-lists/", func_base_project_list_api, name="func_base_project_list_api_view"),
    path("project-details/<int:project_id>/", func_base_project_details_api, name="func_base_project_details_api"),
    path("task-lists/", func_base_task_list_api, name="func_base_task_list_api_view"),
]
