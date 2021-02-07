from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('booking.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')), #Add Django site authentication urls (for login, logout, password management)
                                                         #Using the above method adds automatically URLs with names in square brackets.
]
