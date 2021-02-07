from django.conf.urls import url
from booking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.booking_list, name='index'),
    url(r'^home/$', views.booking_list, name='home'),
    url(r'^booking_list/$', views.booking_list, name='booking_list'),

    url(r'^admin_panel$', views.admin_panel, name='admin_panel'),
    url(r'^room_admin_table/$', views.room_admin_table, name='room_admin_table'),
    url(r'^booking_admin_table/$', views.booking_admin_table, name='booking_admin_table'),
    url(r'^user_admin_table/$', views.user_admin_table, name='user_admin_table'),

    url(r'^booking/(?P<pk>\d+)/$', views.booking_detail, name='booking_detail'),

    url(r'^booking/booking_insert.html$', views.booking_insert, name='booking_insert'),
    url(r'^booking/(?P<pk>\d+)/update/', views.booking_update, name='booking_update'),
    url(r'^booking/(?P<pk>\d+)/delete(?P<admin_table_flag>\d+)', views.booking_delete, name='booking_delete'),

    url(r'^booking/room_insert.html$', views.room_insert, name='room_insert'),
    url(r'^room/(?P<pk>\d+)/update/', views.room_update, name='room_update'),
    url(r'^room/(?P<pk>\d+)/delete(?P<admin_table_flag>\d+)', views.room_delete, name='room_delete'),

    url(r'^user_access_admin_table/$', views.user_access_admin_table, name='user_access_admin_table'),
    url(r'^booking/user_access_insert.html$', views.user_access_insert, name='user_access_insert'),
    url(r'^booking/(?P<pk>\d+)/user_access_update.html$', views.user_access_update, name='user_access_update'),
    url(r'^booking/(?P<pk>\d+)/delete_user_access(?P<admin_table_flag>\d+)', views.user_access_delete, name='user_access_delete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
