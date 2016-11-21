

from django.conf.urls.static import static
from django.conf import settings
from mysite.views import *
from rest_framework import routers


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from mysite.form import  LoginForm


router = routers.DefaultRouter()

# 우리가 만든 API를 자동으로 라우팅합니다.
# 그리고 API 탐색을 위해 로그인 URL을 추가했습니다.




urlpatterns = [
                  url(r'^rest-test', include(router.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^', include('snippets.urls')),
                  url(r'^admin/', include(admin.site.urls)),
                    # 로그인 회원가입 인증부분.
                  url(r'^accounts/', include('django.contrib.auth.urls'),  name='login'),
                  url(r'^accounts/register/',registerView, name='register'),
                  url(r'^signup_ok/', TemplateView.as_view(
                    template_name='home.html'
                    ), name='signup_ok'),

                  url(r'^$', HomeView.as_view(), name='home'),
                  url(r'^mood/', include('mood.urls', namespace='mood')),
                  url(r'^moodcalendar/', include('moodcalendar.urls', namespace='moodcalendar')),


                   url(r'^about/',aboutView) ,

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
