from rest_framework.serializers import ModelSerializer
from taskManagement.models.models import Project, Task
from authenticaion.serializers.serializers import *

class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
    members = UserDetailsSerializer(read_only=True, many=True)
    # project_manager = UserDetailsSerializer(read_only=True)

class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    # project = ProjectDetailsSerializer(read_only=True, many=True)