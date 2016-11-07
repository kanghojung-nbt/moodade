from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [

    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^snippets/', views.snippet_list),
    url(r'^stocks/',views.StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)