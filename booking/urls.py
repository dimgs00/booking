from django.conf.urls import url
from booking import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^home/$', views.home, name='home'),

    url(r'^booking_list/$', views.booking_list, name='booking_list'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^admin_panel.html$', views.admin_panel, name='admin_panel'),

    url(r'^booking/booking_insert.html$', views.booking_insert, name='booking_insert'),

    url(r'^my_booking_list/$', views.my_booking_list, name='my_booking_list'),

    url(r'^booking/(?P<pk>\d+)/$', views.booking_detail, name='booking_detail'),


]
