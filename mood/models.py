from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#기존 테이블 분리
class Emoticon(models.Model):
    mcolor = models.CharField(max_length=40, blank=True, null=True)  # 감정을 나타낼 색깔
    memotion = models.CharField(max_length=100, blank=True, null=True)  # 감정 카테고리
    def __str__(self):
        return self.mcolor + " / " + self.memotion

class Emotion(models.Model):
    category=models.ForeignKey(Emoticon)
    mood_Verb = models.CharField(max_length=100, blank=True, null=True)  # 카테고리 안에 있는 세부단어 ex 화남 -> 개같은 , 빡친,
    mood_Amount = models.FloatField(default=0, null=True)  # 감정수치

@python_2_unicode_compatible
class Mood(models.Model):
    color = models.CharField(max_length=40, blank=True , null= True)   #  감정을 나타낼 색깔
    emotion = models.CharField(max_length=100, blank=True, null=True)  #  감정 카테고리
    mood_Verb = models.CharField(max_length=100, blank=True, null=True) #  카테고리 안에 있는 세부단어 ex 화남 -> 개같은 , 빡친,
    mood_Amount = models.FloatField(default=0, null=True)  #  감정수치
    def __str__(self):
        return " 현재 감정 단어: "  + self.mood_Verb  + "\n현재 감정 : "+self.emotion  + "\n현재 감정 색깔: "+self.color

class moodCalendar(models.Model):
    userid=models.CharField(max_length=20,blank=False,null=False)  #id
    moodDate=models.DateTimeField(auto_now_add=True)    #등록한 날짜
    moodid= models.CharField(max_length=1000)           #저장한 무드 아이디
    color=models.CharField(max_length=20,blank=False,null=False)  #color
    category = models.CharField(max_length=20,blank=False,null=False)  #기분
    startNum=models.FloatField(default=0, null=True)  # 감정수치
    endNum= models.FloatField(default=0, null=True)  # 감정수치


class VerbList(models.Model):   #폼으로 받을 데이터 정의 -> DB에 들어갈 건 아니당.
    verblist=models.TextField(max_length=1000, unique=True)
    def __str__(self):
        return self.verblist

class EmotionText(models.Model):        #사진파일 다운로드할때 볼 글귀
    category=models.CharField(max_length=20,blank=False,null=False)  #기분
    text = models.CharField(max_length=2000,null=False,blank=False)

