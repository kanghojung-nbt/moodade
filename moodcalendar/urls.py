from django.conf.urls import url
from moodcalendar.views import *




urlpatterns = [
    url(r'^$', mycalendar, name='mycalendar'),
]