from django.db import models

from project.models import Project
from user.models import User


class TODO_Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField()
