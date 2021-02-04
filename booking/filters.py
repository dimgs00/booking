from django import forms
from .models import *
import django_filters
import datetime
from django.forms.widgets import SelectDateWidget
from django.forms import ModelForm, Form
import datetime
from django.forms.widgets import SelectDateWidget
from django.forms import ModelForm, Form


class BookingFilter(django_filters.FilterSet):
    # RATING_CHOICES
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    f_category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all().order_by('title'), widget=forms.CheckboxSelectMultiple)
    rating_gte = django_filters.ChoiceFilter(field_name='rating', choices=RATING_CHOICES, lookup_expr='gte')
    rating_lte = django_filters.ChoiceFilter(field_name='rating', choices=RATING_CHOICES, lookup_expr='lte')
    published_datetime_gte = django_filters.DateFilter(field_name='published_datetime', lookup_expr='gte')
    published_datetime_lte = django_filters.DateFilter(field_name='published_datetime', lookup_expr='lte')
