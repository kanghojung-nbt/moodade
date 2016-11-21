from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^keyboard/', views.my_view),
    url(r'^friend/', views.FriendView.as_view()),
    url(r'^chat_room', views.FriendView.as_view()),
    url(r'^message', views.MessageView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

