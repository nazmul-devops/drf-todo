from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.permissions.permissions import IsSuperUser


# Create your views here.
class HealthCheakAPIView(APIView):
    permission_classes = (IsAuthenticated, IsSuperUser)
    def get(self, request, *args, **kwargs):
        try:
            response = {
                "message": "Service is up and running....",
                "version": "v1.0.0",
                "created_by": "Nazmul Islam (Associate DevOps and web developer)",
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
        return Response(
            {"Error": "Internal Server Error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
