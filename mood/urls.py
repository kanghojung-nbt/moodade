

from django.conf.urls import url
from mood.views import *

urlpatterns = [
    url(r'^$', MoodkLV.as_view(), name='index'),
]
