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



class VerbList(models.Model):   #폼으로 받을 데이터 정의 -> DB에 들어갈 건 아니당.
    verblist=models.TextField(max_length=1000, unique=True)
    def __str__(self):
        return self.verblist

class EmotionText(models.Model):        #현재 결과값
    CATEGORY = (
        ('red', '화남'),
        ('purple', '지루함'),
        ('magenta', '혐오스러움'),
        ('green', '무서움'),
        ('yellow', '행복함'),
        ('orange', '흥미'),
        ('blue', '슬퍼요'),
        ('skyblue', '놀라워요'),
    )
    category = models.CharField(max_length=20, null=False, default='', choices=CATEGORY)
    text = models.CharField(max_length=2000,null=False,blank=False)

class DownText(models.Model):
    CATEGORY=(
        ('red','화남'),
        ('purple', '지루함'),
        ('magenta', '혐오스러움'),
        ('green', '무서움'),
        ('yellow', '행복함'),
        ('orange', '흥미'),
        ('blue', '슬퍼요'),
        ('skyblue', '놀라워요'),
    )
    text=models.CharField(max_length=2000,null=False)
    category= models.CharField(max_length=20,null=False, default='',choices=CATEGORY)

    def __str__(self):
        return " \n현재 카테고리: " + self.category +  "\n현재 추천단어 : " + self.text
