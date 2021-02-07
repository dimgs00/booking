from django.contrib import admin
from .models import Booking, UserAccess, Access, Room

admin.site.register(Booking)
admin.site.register(UserAccess)
admin.site.register(Access)
admin.site.register(Room)
