from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=32,
        unique=True,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
