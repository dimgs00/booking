# users/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^user_detail/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^user/(?P<pk>\d+)/user_update.html$', views.user_update, name='user_update'),
    url(r'^user_change_password/(?P<pk>\d+)$', views.user_change_password, name='user_change_password'),
    url(r'^user/(?P<pk>\d+)/user_delete(?P<admin_table_flag>\d+)', views.user_delete, name='user_delete'),
    url(r'^user/(?P<pk>\d+)/user_category_insert.html$', views.user_category_insert, name='user_category_insert'),
]
