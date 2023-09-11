from django.db import models
from core.models.models import BaseTimeStampedModel
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Project(BaseTimeStampedModel):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    project_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="project_project_manager",
    )
    members = models.ManyToManyField(User, blank=True, related_name="project_members")
    
    def __str__(self):
        return self.name
    

class Task(BaseTimeStampedModel):
    TASK_STATUS_OPTIONS = (
        ("done", "Done"),
        ("active", "Active"),
        ("finished", "Finished"),
    )
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=TASK_STATUS_OPTIONS, default="active"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_created_by"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="task_project"
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'project', 'created_by'],
                                    name='unique_name_project_created_by')
        ]

    def __str__(self):
        return self.name
    