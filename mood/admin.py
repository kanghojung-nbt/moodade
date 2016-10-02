from django.contrib import admin
from mood.models import Mood

# Register your models here.

class MoodAdmin(admin.ModelAdmin):
    list_display = ('color', 'emotion', 'mood_Verb','mood_Amount')

admin.site.register(Mood , MoodAdmin)

