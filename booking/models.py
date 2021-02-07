from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


#Type of a user with access rights. For example: "Administrator" or "User"
class Access(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Room(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    photo = models.ImageField('Image', blank=True, null=True, default='media/no_image.png')

    def __str__(self):
        return self.title


class Booking(models.Model):
    date_from = models.DateField('From', default=datetime.now, blank=False, null=False)
    date_to = models.DateField('To', default=datetime.now, blank=False, null=False)
    f_room = models.ForeignKey(Room, verbose_name='Room', default='0', on_delete=models.CASCADE)
    f_user = models.ForeignKey(get_user_model(), verbose_name='User', default='0', on_delete=models.CASCADE)


class UserAccess(models.Model):
    f_user = models.ForeignKey(get_user_model(), verbose_name='User', default='0', on_delete=models.CASCADE)
    f_access = models.ForeignKey(Access, verbose_name='Access rights', default='0', on_delete=models.CASCADE)
