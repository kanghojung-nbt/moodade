from django.conf.urls import url
from moodcalendar.views import *

urlpatterns = [
    url(r'^$', mycalendar, name='mycalendar'),
    url(r'^calendar/', calendar),
    url(r'^ajaxCalendr/', ajaxCalendr),
]
