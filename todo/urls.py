from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from core import urls as core_urls
from taskManagement import urls as taskManagement_urls

urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend</h1>", content_type="text/html")),
    path('admin/', admin.site.urls),
    path('api/core/', include(core_urls)),
    path('api/', include(taskManagement_urls)),
]
