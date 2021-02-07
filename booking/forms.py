from django import forms
from .models import Booking, UserAccess, Room
from bootstrap_datepicker_plus import DatePickerInput


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["title"]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date_from", "date_to", "f_room", "f_user"]
        widgets = {
            'date_from':DatePickerInput(),
            'date_to':DatePickerInput()
        }


class UserAccessForm(forms.ModelForm):
    class Meta:
        model = UserAccess
        fields = ["f_user", "f_access"]
