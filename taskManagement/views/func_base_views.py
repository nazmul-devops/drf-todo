import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from taskManagement.models.models import *
from taskManagement.serializers.serializers import ProjectListSerializer, TaskListSerializer
User = get_user_model()
logger = logging.getLogger('__name__')
@api_view(["GET"])
def func_base_project_list_api(request, *args, **kwargs):
    try:
        project_lists = Project.objects.all()
        # response = []
        # for project in project_lists:
        #     data = {
        #         "id": project.id,
        #         "name": project.name,
        #     }
        #     response.append(data)
        serializer = ProjectListSerializer(instance=project_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as ex:
        logger.error(str(ex), exe_info=True)
    return Response({"error": "INTERNAL_SERVER_ERROR"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["GET"])
def func_base_project_details_api(request, project_id, *args, **kwargs):
    try:
        project_details = Project.objects.filter(pk=project_id).first()
        serializer = ProjectListSerializer(instance=project_details)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as ex:
        logger.error(str(ex), exe_info=True)
    return Response({"error": "INTERNAL_SERVER_ERROR"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def func_base_task_list_api(request, *args, **kwargs):
    try:
        task_lists = Task.objects.all()
        task_serializer = TaskListSerializer(instance=task_lists, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)

    except Exception as ex:
        logger.error(str(ex), exe_info=True)
    return Response({"error": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)