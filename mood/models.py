from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Mood(models.Model):
    color = models.CharField(max_length=40, blank=True , null= True)   #  감정을 나타낼 색깔
    emotion = models.CharField(max_length=100, blank=True, null=True)  #  감정 카테고리
    mood_Verb = models.CharField(max_length=100, blank=True, null=True) #  카테고리 안에 있는 세부단어 ex 화남 -> 개같은 , 빡친,
    mood_Amount = models.FloatField(default=0, null=True)  #  감정수치

    def __str__(self):
        return self.mood_Verb + self.emotion + self.color
