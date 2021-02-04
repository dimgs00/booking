# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
# from request_app.models import Access

class CustomUser(AbstractUser):
    # add additional fields in here
    username = models.CharField('Όνομα χρήστη', unique=True, max_length=50, blank=False, null=False)
    email = models.EmailField('Ηλ. ταχυδρομείο*', max_length=50, blank=True, null=False)
    first_name = models.CharField('Όνομα*', max_length=50, blank=False, null=False)
    last_name = models.CharField('Επώνυμο*', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.username
