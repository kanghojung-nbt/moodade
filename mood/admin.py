from django.contrib import admin
from mood.models import Mood,Emoticon,Emotion,EmotionText,DownText

# Register your models here.

class MoodAdmin(admin.ModelAdmin):
    list_display = ('color', 'emotion', 'mood_Verb','mood_Amount')

class EmoticonAdmin(admin.ModelAdmin):
    list_display = ('mcolor','memotion')
    
class EmotionAdmin(admin.ModelAdmin):
    list_display = ('category','mood_Verb','mood_Amount')


class EmotionTextAdmin(admin.ModelAdmin):
    list_display =('category', 'text')
class DownTextAdmin(admin.ModelAdmin):
    list_display = ('category','text')


admin.site.register(Mood , MoodAdmin)
admin.site.register(Emoticon, EmoticonAdmin)

admin.site.register(EmotionText, EmotionTextAdmin)
admin.site.register(DownText, DownTextAdmin)

# userid = models.CharField(max_length=20, blank=False, null=False)  # id
# moodDate = models.DateTimeField(auto_now_add=True)  # 등록한 날짜
# moodid = models.CharField(max_length=1000)  # 저장한 무드 아이디
# color = models.CharField(max_length=20, blank=False, null=False)  # color
# category = models.CharField(max_length=20, blank=False, null=False)  # 기분
# startNum = models.FloatField(default=0, null=True)  # 감정수치
# endNum = models.FloatField(default=0, null=True)  # 감정수치

