# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField('Username*', unique=True, max_length=50, blank=False, null=False)
    first_name = models.CharField('First Name*', max_length=50, blank=False, null=False)
    last_name = models.CharField('Last Name*', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.username
