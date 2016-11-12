from django.contrib import admin
from moodcalendar.models import *
class MyCalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'moodDate', 'moodid', 'color', 'category', 'maxNum', 'minNum')




admin.site.register(MyCalendar, MyCalendarAdmin)

# Register your models here.
