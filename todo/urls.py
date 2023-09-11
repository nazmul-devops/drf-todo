from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import urls as core_urls
from taskManagement import urls as taskManagement_urls
from authenticaion import urls as authenticaion_urls


schema_view = get_schema_view(
   openapi.Info(
      title="DRF ToDo Backend API",
      default_version='v1.0.0',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend</h1>", content_type="text/html")),
    path('admin/', admin.site.urls),
    path('api/core/', include(core_urls)),
    path('api/task/', include(taskManagement_urls)),
    path('api/auth/', include(authenticaion_urls)),
]

swagger_urlpatterns = [
   # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += swagger_urlpatterns


