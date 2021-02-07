from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^user/(?P<pk>\d+)/user_update.html$', views.user_update, name='user_update'),
    url(r'^user/(?P<pk>\d+)/user_delete(?P<admin_table_flag>\d+)', views.user_delete, name='user_delete'),
]
