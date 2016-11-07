from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^keyboard/', views.ButtonList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^stocks/',views.StockList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

