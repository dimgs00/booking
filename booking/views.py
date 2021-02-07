from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from .forms import BookingForm, UserAccessForm, RoomForm
from django.shortcuts import render, get_object_or_404 # redirect,


def home(request):
    return render(request, 'booking/index.html', {})


def booking_list(request, null=None):
    room_id = request.GET.get('room_id', '')
    user_authenticated = request.user.is_authenticated
    user_authenticated_pk = request.user.pk

    if user_authenticated:
        try:
            user_access_object = UserAccess.objects.get(f_user=user_authenticated_pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            print("DoesNotExist")
            return render(request, 'booking/forbidden_access.html')
    else:
        print("empty")


    rooms_list = []
    booking_dict = {}
    rooms_distinct = Room.objects.all().distinct().order_by('title')
    i = 0
    for room in rooms_distinct:
        rooms_list.append(room.title)
        booking_objects_by_room_id = Booking.objects.filter(f_room = room.id)
        booking_dict[i] = booking_objects_by_room_id
        i += 1

    return render(request, 'booking/booking_list.html', locals())


def admin_panel(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')

    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    return render(request, 'booking/admin_panel.html', locals())


def user_admin_table(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    user_objects = get_user_model().objects.all().order_by('username')
    booking_list = Booking.objects.all()

    return render(request, 'booking/user_admin_table.html', locals())


def user_access_admin_table(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')

    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        try:
            user_access_object = UserAccess.objects.get(f_user=username_authenticated_id)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            print("DoesNotExist")
            return render(request, 'booking/forbidden_access.html')    ###############################################################

    user_access_objects = UserAccess.objects.all().order_by('f_user')
    booking_list = Booking.objects.all()

    return render(request, 'booking/user_access_admin_table.html', locals())


def booking_insert(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')

    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    ###################################################################

    booking_flag = request.GET.get('booking_flag', '')
    try:
        booking_flag = int(booking_flag)
    except:
        booking_flag = 1

    booking_objects = Booking.objects.all()

    booking_list = Booking.objects.all()

    # Submit Form
    if request.method == 'GET':
        error_photo = False
        form = BookingForm()
    else:
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            f_room = form.cleaned_data['f_room']
            f_user = form.cleaned_data['f_user']
            Booking.objects.create(
                date_from = date_from,
                date_to = date_to,
                f_room = f_room,
                f_user = f_user
            )
            return render(request, 'booking/booking_successful_insert.html', locals())
    return render(request, 'booking/booking_insert.html', locals())


def booking_detail(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')

    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")


    booking_flag = request.GET.get('booking_flag', '')
    try:
        booking_flag = int(booking_flag)
    except:
        booking_flag = 1

    room_object = get_object_or_404(Room, pk=pk)
    booking_objects = Booking.objects.filter(f_room=pk)
    booking_list = Booking.objects.all()

    return render(request, 'booking/booking_detail.html', locals())


def booking_update(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")


    request_flag = request.GET.get('request_flag', '')
    try:
        request_flag = int(request_flag)
    except:
        request_flag = 1

    booking_list = Booking.objects.all()
    booking_obj = get_object_or_404(Booking, pk=pk)

    # Submit Form
    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES, instance=booking_obj)
        if form.is_valid():
            booking_obj.save()
            return render(request, 'booking/booking_successful_updating.html', locals())
    else:
        form = BookingForm(instance=booking_obj)

    return render(request, 'booking/booking_update.html', locals())


def booking_admin_table(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")


    booking_flag = request.GET.get('booking_flag', '')
    try:
        booking_flag = int(booking_flag)
    except:
        booking_flag = 1


    booking_objects = Booking.objects.all().order_by('-date_from')
    booking_list = Booking.objects.all()

    return render(request, 'booking/booking_admin_table.html', locals())


def booking_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    booking_flag = 1
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")


    booking_flag = request.GET.get('booking_flag', '')
    try:
        booking_flag = int(booking_flag)
    except:
        booking_flag = 1


    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False


    booking_objects = Booking.objects.all()
    if admin_table_flag != False:
        Booking.objects.get(pk=pk).delete()
        return render(request, 'booking/booking_admin_table.html', locals())
    else:
        Booking.objects.get(pk=pk).delete()
        return render(request, 'booking/booking_list.html', locals())

    return render(request, 'booking/booking_list.html', locals())


def user_access_insert(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    booking_list = Booking.objects.all()

    # Submit Form
    if request.method == 'GET':
        form = UserAccessForm()
    else:
        form = UserAccessForm(request.POST)
        if form.is_valid():
            f_user = form.cleaned_data['f_user']
            f_access = form.cleaned_data['f_access']

            str_f_user = str(f_user)
            if(str_f_user != "admin"):
                UserAccess.objects.create(
                    f_user = f_user,
                    f_access = f_access,
                )
                return render(request, 'booking/user_access_successful_insert.html', locals())
            else:
                user_access_object = get_object_or_404(UserAccess, f_user=1)
                return render(request, 'booking/forbidden_insert_access_privileges.html', locals())

    return render(request, 'booking/user_access_insert.html', locals())


def user_access_update(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    user_access_object = get_object_or_404(UserAccess, pk=pk)
    booking_list = Booking.objects.all()

    # Submit Form
    if request.method == "POST":
        form = UserAccessForm(request.POST, instance=user_access_object)
        if form.is_valid():
            f_user = form.cleaned_data['f_user']
            str_f_user = str(f_user)
            if(str_f_user != "admin"):
                user_access_object.save()
                return render(request, 'booking/user_access_successful_updating.html', locals())
            else:
                user_access_object = UserAccess.objects.get(f_user=1)
                return render(request, 'booking/forbidden_update_access_privileges.html', locals())
    else:
        form = UserAccessForm(instance=user_access_object)

    return render(request, 'booking/user_access_update.html', locals())


def user_access_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        try:
            user_access_object = UserAccess.objects.get(f_user=username_authenticated_id)
        except MultipleObjectsReturned:
            print("MultipleObjectsReturned")
    else:
        print("empty")


    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False

    user_access_object = UserAccess.objects.get(f_user=1)
    user_access_objects = UserAccess.objects.all()
    UserAccess.objects.get(pk=pk).delete()

    return render(request, 'booking/user_access_admin_table.html', locals())


def room_admin_table(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_flag = request.GET.get('room_flag', '')
    try:
        room_flag = int(room_flag)
    except:
        room_flag = 1

    room_objects = Room.objects.all()
    room_list = Room.objects.all()

    return render(request, 'booking/room_admin_table.html', locals())


def room_insert(request):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_objects = Room.objects.all()
    room_list = Room.objects.all()

    # Submit Form
    if request.method == 'GET':
        form = RoomForm()
    else:
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            Room.objects.create(
                title = title,
            )
            return render(request, 'booking/room_successful_insert.html', locals())
    return render(request, 'booking/room_insert.html', locals())


def room_update(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_flag = request.GET.get('room_flag', '')
    try:
        room_flag = int(room_flag)
    except:
        room_flag = 1

    room_list = Room.objects.all()
    room_obj = get_object_or_404(Room, pk=pk)

    # Submit Form
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES, instance=room_obj)
        if form.is_valid():
            room_obj.save()
            return render(request, 'booking/room_successful_updating.html', locals())
    else:
        form = RoomForm(instance=room_obj)

    return render(request, 'booking/room_update.html', locals())


def room_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    room_flag = 1
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_flag = request.GET.get('room_flag', '')
    try:
        room_flag = int(room_flag)
    except:
        room_flag = 1

    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False


    room_objects = Room.objects.all()
    if admin_table_flag != False:
        Room.objects.get(pk=pk).delete()
        return render(request, 'booking/room_admin_table.html', locals())
    else:
        Room.objects.get(pk=pk).delete()
        return render(request, 'booking/room_list.html', locals())

    return render(request, 'booking/room_list.html', locals())


def room_delete(request, pk, admin_table_flag):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    room_flag = 1
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_flag = request.GET.get('room_flag', '')
    try:
        room_flag = int(room_flag)
    except:
        room_flag = 1

    try:
        admin_table_flag = int(admin_table_flag)
    except:
        admin_table_flag = False


    room_objects = Room.objects.all()
    Room.objects.get(pk=pk).delete()

    return render(request, 'booking/room_admin_table.html', locals())


def room_update(request, pk):
    username_authenticated_id = request.GET.get('username_authenticated_id', '')
    try:
        username_authenticated_id = int(username_authenticated_id)
    except:
        username_authenticated_id = False

    if username_authenticated_id != False:
        user_access_object = get_object_or_404(UserAccess, f_user=username_authenticated_id)
    else:
        print("empty")

    room_flag = request.GET.get('room_flag', '')
    try:
        room_flag = int(room_flag)
    except:
        room_flag = 1

    room_list = Room.objects.all()
    room_obj = get_object_or_404(Room, pk=pk)

    # Submit Form
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES, instance=room_obj)
        if form.is_valid():
            room_obj.save()
            return render(request, 'booking/room_successful_updating.html', locals())
    else:
        form = RoomForm(instance=room_obj)
    return render(request, 'booking/room_update.html', locals())
