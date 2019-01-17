from django.conf.urls import url
from django.contrib import admin
from rsvpapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CreateRsvp.as_view(), name='create_rsvp'),
    url(r'^check_list/$', CheckList.as_view(), name='check_list'),
]
