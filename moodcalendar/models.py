
from django.db import models

from django.conf import settings
# Create your models here.

#기존 테이블 분리
class MyCalendar(models.Model):
    user = models.CharField(max_length=40)
    moodDate = models.DateTimeField(auto_now_add=False)  # 등록한 날짜
    moodid = models.CharField(max_length=1000)  # 저장한 무드 아이디
    color = models.CharField(max_length=20, blank=False, null=False)  # color
    category = models.CharField(max_length=20, blank=False, null=False)  # 기분
    maxNum = models.FloatField(default=0, null=True)  # 최대 감정수치
    minNum = models.FloatField(default=0, null=True)  # 최소 감정수치
    def __str__(self):
        return   "현재 감정 색깔: "+self.color+"\n"


