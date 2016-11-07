from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV
from mysite.views import *
from django.conf.urls import url, include
from rest_framework import routers
from mysite import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'keyboard', views.GroupViewSet)

# 우리가 만든 API를 자동으로 라우팅합니다.
# 그리고 API 탐색을 위해 로그인 URL을 추가했습니다.


urlpatterns = [
                  url(r'^rest-test', include(router.urls)),

                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^', include('snippets.urls')),


                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^accounts/', include('django.contrib.auth.urls')),
                  url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
                  url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

                  url(r'^$', HomeView.as_view(), name='home'),
                  url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
                  url(r'^blog/', include('blog.urls', namespace='blog')),
                  url(r'^photo/', include('photo.urls', namespace='photo')),
                  url(r'^mood/', include('mood.urls', namespace='mood')),
                  url(r'^moodcalendar/', include('moodcalendar.urls', namespace='moodcalendar')),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
