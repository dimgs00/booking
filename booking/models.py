from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Access(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Booking(models.Model):
    title = models.CharField('Title', max_length=50, blank=False, null=False)
    description = models.TextField('Description', max_length=1000, blank=True, null=True)
    published_datetime = models.DateTimeField('Date (YYYY-MM-DD)', default=datetime.now, blank=True, null=True)
    photo = models.ImageField('Image', blank=True, null=True, default='noimage.png')
    # rating = models.PositiveIntegerField('Βαθμολογία(1-5)', default='0', validators=[MinValueValidator(1),MaxValueValidator(5)], blank=True, null=True)
    counter_popularity = models.PositiveIntegerField('Views', default=1, blank=True, null=True)
    f_category = models.ForeignKey(Category, default='0', on_delete=models.CASCADE, verbose_name='Category')
    f_user = models.ForeignKey(get_user_model(), verbose_name='User', default='0', on_delete=models.CASCADE)

    def publish(self):
        self.published_datetime = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class UserAccess(models.Model):
    f_user = models.ForeignKey(get_user_model(), verbose_name='User', default='0', on_delete=models.CASCADE)
    f_access = models.ForeignKey(Access, verbose_name='Access rights', default='0', on_delete=models.CASCADE)
