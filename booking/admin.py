from django.contrib import admin
from .models import Booking, Category, UserAccess, Access

admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(UserAccess)
admin.site.register(Access)
