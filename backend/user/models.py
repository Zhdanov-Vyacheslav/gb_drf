from django.db import models


class User(models.Model):
    email = models.EmailField(
        max_length=32,
        unique=True,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
