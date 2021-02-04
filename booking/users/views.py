# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from request_app.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model # Custom model for users
from request_app.models import *
from request_app.filters import RequestFilter
from django.contrib.auth.models import User


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# USERS' DETAILS
def user_detail(request, pk):
    user_object = get_object_or_404(get_user_model(), pk=pk)
    user_category_objects = UserCategory.objects.filter(f_user = pk)


    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
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


    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()


    #################### FILTERS.py ####################
    ########## Painting Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0
    # request_object.counter_popularity = request_object.counter_popularity + 1
    # request_object.save()

    return render(request, 'user_detail.html', locals())


def user_update(request, pk):
    user_object = get_object_or_404(get_user_model(), pk=pk)


    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
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


    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()


    #################### FILTERS.py ####################
    ########## Painting Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0
    # request_object.counter_popularity = request_object.counter_popularity + 1
    # request_object.save()


    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user_object)
        if form.is_valid():
            user_object.save()
            # return redirect('user_admin_table')
            return render(request, 'user_successful_updating.html', locals())
    else:
        form = CustomUserChangeForm(instance=user_object)

    return render(request, 'user_update.html', locals())


def user_change_password(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)

    user_object = get_user_model().objects.get(pk=pk)
    new_password = request.POST.get("new_password")
    # user_object = get_user_model().objects.get(username__exact='maria')
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, instance=user_object)
        user_object.set_password(new_password)
        user_object.save()
        return redirect('user_admin_table')
    else:
        form = ChangePasswordForm(instance=user_object)
        return render(request, 'user_change_password.html', locals())

    return redirect('user_admin_table')


def user_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    ####################################################################

    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False

    user_objects = get_user_model().objects.all().order_by('username')
    # Checking if delete action was from administrator's table page
    if admin_table_flag != False:
        get_object_or_404(get_user_model(), pk=pk).delete()
        return render(request, 'request_app/user_admin_table.html', locals())
    else:
        get_object_or_404(get_user_model(), pk=pk).delete()
        return render(request, 'request_app/request_list.html', locals())

    return render(request, 'request_app/request_list.html', locals())


def user_category_insert(request, pk):
    user_object = get_object_or_404(get_user_model(), pk=pk)

    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
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


    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()


    #################### FILTERS.py ####################
    ########## Painting Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0
    # request_object.counter_popularity = request_object.counter_popularity + 1
    # request_object.save()


    if request.method == 'GET':
        form = UserCategoryForm(instance=user_object)
    else:
        form = UserCategoryForm(request.POST, instance=user_object)
        if form.is_valid():
            # f_user = form.cleaned_data['f_user']
            f_category = form.cleaned_data['f_category']
            username_current = request.POST.get('username_current')
            user_object = get_object_or_404(get_user_model(), pk=pk)
            UserCategory.objects.create(
                f_user = user_object,
                f_category = f_category
            )
            return HttpResponseRedirect(reverse('user_admin_table'))
    return render(request, 'user_category_insert.html', locals())
