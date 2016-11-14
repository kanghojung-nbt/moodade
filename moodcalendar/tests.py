from moodcalendar.models import  *
from datetime import datetime
# Create your tests here.
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,5), moodid='1,2,3', color="orange",category="happy",maxNum=8.3,minNum=2.4)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,7), moodid='1,2,3', color="yellow",category="happy",maxNum=6.3,minNum=4.8)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,9), moodid='1,2,3', color="yellow",category="happy",maxNum=8.3,minNum=2.1)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,11), moodid='1,2,3', color="purple",category="happy",maxNum=9.1,minNum=1.3)
fb.save()
