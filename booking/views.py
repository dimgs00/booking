from .models import *
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from .filters import BookingFilter



def home(request):
    return render(request, 'booking/index.html', {})

# BOOKING LIST
def booking_list(request, null=None):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        try:
            user_access_object = UserAccess.objects.get(f_user=username_authenticated_id)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            print("DoesNotExist")
            return render(request, 'booking/forbidden_access.html')
    else:
        print("empty")

    ###################################################################

    booking_flag = request.GET.get('booking_flag', '')
    # Checking if each booking_flag is 1 or not
    try:
        booking_flag = int(booking_flag)
    except:
        booking_flag = 1

    ###################################################################

    # Get IDs and text(search field) from template "booking_list.html"
    txt = request.GET.get('txt', '') # Search text field
    complex_filters_status = request.GET.get('complex_filters_status', '')
    category_id = request.GET.get('category_id', '')

    # Checking if each id is valid or not
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'
    try:
        category_id = int(category_id)
    except:
        category_id = False

    ########################################################################

    # Checking if an ID is valid or not
    if category_id != False:
        booking_objects = Booking.objects.filter(f_category = category_id)
    else:
        if txt == '':
            booking_objects = Booking.objects.all().order_by('-published_datetime')
        else:
            booking_objects = Booking.objects.filter(Q(title__icontains=txt) | Q(description__icontains=txt) |
                                                     Q(f_category__title__icontains=txt)).order_by('-published_datetime')
    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')

    #################### FILTERS.py ####################
    ########## Booking Filter by "filters.py" ##########
    booking_list = Booking.objects.all()
    booking_filter = BookingFilter(request.GET, queryset=booking_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        booking_objects = booking_filter.qs
        complex_filters_status = 0

    # Final RETURN
    return render(request, 'booking/booking_list.html', locals())


def admin_panel(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
        # user_access_object = UserAccess.objects.filter(f_user=username_authenticated_id)
    else:
        print("empty")

    ###################################################################

    ##### Complex Filters #####
    complex_filters_status = request.GET.get('complex_filters_status', '')

    # Checking if each id is valid or not
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'

    #################### FILTERS.py ####################
    ########## Request Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0

    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()

    return render(request, 'request_app/admin_panel.html', locals())



def booking_insert(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
        # user_access_object = UserAccess.objects.filter(f_user=username_authenticated_id)
    else:
        print("empty")

    ###################################################################

    request_flag = request.GET.get('request_flag', '')
    # Checking if each request_flag is 1 or not
    try:
        request_flag = int(request_flag)
    except:
        request_flag = 1

    ####################################################################
    request_objects = Request.objects.all()

    ##### Complex Filters #####
    complex_filters_status = request.GET.get('complex_filters_status', '')

    # Checking if each id is valid or not
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'

    #################### FILTERS.py ####################
    ########## Request Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0

    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()


    # Submit Form
    if request.method == 'GET':
        error_photo = False
        form = RequestForm()
    else:
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            coordinates = form.cleaned_data['coordinates']
            photo = form.cleaned_data['photo']
            # counter_popularity = 1
            f_priority = form.cleaned_data['f_priority']
            # f_stage = form.cleaned_data['f_stage']
            f_stage = get_object_or_404(Stage, pk=1)
            f_category = form.cleaned_data['f_category']
            username_current = request.POST.get('username_current')
            user_object = get_object_or_404(get_user_model(), username=request.user.username)
            Request.objects.create(
                title = title,
                description = description,
                coordinates = coordinates,
                photo = photo,
                # counter_popularity = counter_popularity,
                f_priority = f_priority,
                f_stage = f_stage,
                f_category = f_category,
                f_user = user_object
            )
            error_photo = False
            # return HttpResponseRedirect(reverse('request_list'))
            return render(request, 'request_app/request_successful_insert.html', locals())
        error_photo = True
    return


# MY BOOKING LIST
def my_booking_list(request, null=None):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    # Checking if each id is valid or not
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        # user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
        try:
            user_access_object = UserAccess.objects.get(f_user=username_authenticated_id)
            # user_access_object = UserAccess.objects.filter(f_user=username_authenticated_id)
        except UserAccess.DoesNotExist:
            print("DoesNotExist")
    else:
        print("empty")

    ###################################################################

    request_flag = request.GET.get('request_flag', '')
    # Checking if each request_flag is 1 or not
    try:
        request_flag = int(request_flag)
    except:
        request_flag = 1

    ###################################################################
    my_request_objects = Request.objects.filter(f_user=username_authenticated_id).order_by('-published_datetime')


    ##### Complex Filters #####
    complex_filters_status = request.GET.get('complex_filters_status', '')

    # Checking if each id is valid or not
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'

    #################### FILTERS.py ####################
    ########## Request Filter by "filters.py" ##########
    request_list = Request.objects.all().order_by('-published_datetime')
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0

    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()

    # Final RETURN
    return render(request, 'request_app/my_request_list.html', locals())


# BOOKINGS DETAILS
def booking_detail(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')

    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
        # user_access_object = UserAccess.objects.filter(f_user=username_authenticated_id)
    else:
        print("empty")

    ###################################################################

    request_flag = request.GET.get('request_flag', '')
    # Checking if each request_flag is 1 or not
    try:
        request_flag = int(request_flag)
    except:
        request_flag = 1

    #####################################################################

    request_object = get_object_or_404(Request, pk=pk)

    ##### Complex Filters #####
    complex_filters_status = request.GET.get('complex_filters_status', '')

    # Checking if each id is valid or not
    try:
        complex_filters_status = int(complex_filters_status)
    except:
        complex_filters_status = 'empty'

    try:
        request_comment_object = Comment.objects.filter(f_request=request_object.pk)
        go = True
        # go = int(request_comment_object.pk)
    except Comment.DoesNotExist:
        request_comment_object = 0
        go = False

    # CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            username_authenticated_id_post = request.POST.get("username_authenticated_id_post")
            # Checking if each id is valid or not
            # print("id=", username_authenticated_id_post)

            try:
                username_authenticated_id_post = int(username_authenticated_id_post)
            except:
                username_authenticated_id_post = False

            if username_authenticated_id_post != False:
                user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id_post)
                # user_access_object = UserAccess.objects.filter(f_user=username_authenticated_id)
            else:
                print("empty")

            #################################################################

            username_current = request.POST.get("username_current")
            user_object = get_object_or_404(get_user_model(), username=username_current)
            comments_current = form.cleaned_data['comments']
            Comment.objects.create(comments=comments_current, f_request=request_object, f_user=user_object)
            form = CommentForm()
            return render(request, 'request_app/request_detail.html', locals())
    else:
        form = CommentForm()

    #################### DISTINCT OBJECTS ####################
    #Distinct categories
    categories_distinct = Category.objects.all().distinct().order_by('title')
    stages_distinct = Stage.objects.all().distinct()
    priorities_distinct = Priority.objects.all()

    #################### FILTERS.py ####################
    ########## Request Filter by "filters.py" ##########
    request_list = Request.objects.all()
    request_filter = RequestFilter(request.GET, queryset=request_list)

    ########## COMPLEX filters ("filters.py") vs STANDARD filters #########
    if complex_filters_status != 'empty':
        request_objects = request_filter.qs
        complex_filters_status = 0

    request_object.counter_popularity = request_object.counter_popularity + 1
    request_object.save()
    return render(request, 'request_app/request_detail.html', locals())
