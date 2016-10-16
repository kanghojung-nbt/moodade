from django.contrib import admin
from mood.models import Mood,Emoticon,Emotion

# Register your models here.

class MoodAdmin(admin.ModelAdmin):
    list_display = ('color', 'emotion', 'mood_Verb','mood_Amount')

class EmoticonAdmin(admin.ModelAdmin):
    list_display = ('mcolor','memotion')
    
class EmotionAdmin(admin.ModelAdmin):
    list_display = ('category','mood_Verb','mood_Amount')

admin.site.register(Mood , MoodAdmin)
admin.site.register(Emoticon, EmoticonAdmin)
admin.site.register(Emotion, EmotionAdmin)

