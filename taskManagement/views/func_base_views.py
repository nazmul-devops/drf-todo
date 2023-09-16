import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from taskManagement.models.models import *
from taskManagement.serializers.serializers import (ProjectListSerializer,
                                                    TaskListSerializer,
                                                    ProjectCreateUpdateSerializer)
User = get_user_model()
logger = logging.getLogger('__name__')


@api_view(["GET"])
def func_base_project_list_api(request, *args, **kwargs):
    try:
        project_lists = Project.objects.filter(status='active')
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


@api_view(["POST"])
def func_base_project_create_api(request,  *args, **kwargs):
    try:
        data = request.data
        serializer = ProjectCreateUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:
        logger.error(str(ex), exe_info=True)
    return Response({"error": "INTERNAL_SERVER_ERROR"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def func_base_project_update_api(request, project_id, *args, **kwargs):
    try:
        project_update = Project.objects.filter(pk=project_id).first()
        if not project_update:
            return Response([], status=status.HTTP_204_NO_CONTENT)
        serializer = ProjectCreateUpdateSerializer(instance=project_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as ex:
        logger.error(str(ex), exe_info=True)
    return Response({"error": "INTERNAL_SERVER_ERROR"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def func_base_project_delete_api(request, project_id, *args, **kwargs):
    try:
        try:
            Project.objects.filter(id=project_id).update(status='finished')
            response_data = {"message": "Project deleted successfully"}
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            # Handle the case where the project with the given ID does not exist
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
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

# @api_view(["POST"])
# def func_base_task_list_api(request, *args, **kwargs):
#     try:
#         task_lists = Task.objects.all()
#         task_serializer = TaskListSerializer(instance=task_lists, many=True)
#         return Response(task_serializer.data, status=status.HTTP_200_OK)
#
#     except Exception as ex:
#         logger.error(str(ex), exe_info=True)
#     return Response({"error": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)