from django.conf.urls import include, url
from django.contrib import admin
from libs.views import *

urlpatterns = [
   url(r'^', index, name='index'),
   # url(r'^user-details/(?P<id>.*)$', user_details, name='user-details'),
]