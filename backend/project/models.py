from django.db import models

from user.models import User


class Project(models.Model):
    name = models.CharField(max_length=32)
    repository = models.URLField(max_length=128, default='')
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.name
