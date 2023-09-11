from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('', lambda request: HttpResponse("<h1 style='text-align: center; margin-top: 30px;'>Welcome To ToDo Backend API Authentication APP</h1>", content_type="text/html")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]