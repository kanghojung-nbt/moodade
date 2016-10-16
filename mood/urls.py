from django.conf.urls import url
from mood.views import *


urlpatterns = [
    # url(r'(?P<emoticon>[a-z]{3,16})/$',  MoodLV.as_view(), name='index'),
    url(r'^emoticon/(?P<pEmoticon>.+)',  mood_verb ),
    url(r'^result/',  mood_form),


]
