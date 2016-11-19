from django.conf.urls import url
from moodcalendar.views import *

urlpatterns = [
    url(r'^$', mycalendar, name='mycalendar'),
    url(r'^calendar/', calendar),
    url(r'^write/', makeOrUpdateMemo),
    url(r'^read/', readMemo),

    url(r'^ajaxCalendr/', ajaxCalendr),
]
