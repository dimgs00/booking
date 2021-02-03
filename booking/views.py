from django.shortcuts import render

def booking_list(request):
    return render(request, 'booking/booking_list.html', {})
