from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from booking.forms import *
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model # Custom model for users
from booking.models import *


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('booking_list')
    template_name = 'booking/signup.html'


def user_update(request, pk):
    user_object = get_object_or_404(get_user_model(), pk=pk)

    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)


    complex_filters_status = request.GET.get('complex_filters_status', '')
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'

    booking_list = Booking.objects.all()

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user_object)
        if form.is_valid():
            user_object.save()
            return render(request, 'booking/user_successful_updating.html', locals())
    else:
        form = CustomUserChangeForm(instance=user_object)

    return render(request, 'booking/user_update.html', locals())


def user_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False

    user_objects = get_user_model().objects.all().order_by('username')
    # Checking if delete action was from administrator's table page
    if admin_table_flag != False:
        get_object_or_404(get_user_model(), pk=pk).delete()
        return render(request, 'booking/user_admin_table.html', locals())
    else:
        get_object_or_404(get_user_model(), pk=pk).delete()
        return render(request, 'booking/booking_list.html', locals())

    return render(request, 'booking/booking_list.html', locals())
