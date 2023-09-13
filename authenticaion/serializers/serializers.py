from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from taskManagement.models.models import Project

User = get_user_model()


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

