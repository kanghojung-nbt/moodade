from moodcalendar.models import  *
from datetime import datetime
# Create your tests here.
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,1), moodid='1,2,3', color="orange",category="happy",maxNum=8.3,minNum=2.4)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,2), moodid='1,2,3', color="yellow",category="happy",maxNum=6.3,minNum=1.8)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,3), moodid='1,2,3', color="blue",category="happy",maxNum=8.3,minNum=2.1)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,4), moodid='1,2,3', color="purple",category="happy",maxNum=9.1,minNum=1.3)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,6), moodid='1,2,3', color="orange",category="happy",maxNum=8.3,minNum=2.4)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,8), moodid='1,2,3', color="magenta",category="슬픔",maxNum=8.3,minNum=4.8)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,9), moodid='1,2,3', color="red",category="happy",maxNum=2.3,minNum=0.1)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,10), moodid='1,2,3', color="purple",category="happy",maxNum=9.1,minNum=1.3)
fb.save()

fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,13), moodid='1,2,3', color="blue",category="happy",maxNum=8.3,minNum=2.4)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,14), moodid='1,2,3', color="purple",category="happy",maxNum=3.3,minNum=1.8)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,16), moodid='1,2,3', color="yellow",category="happy",maxNum=7.3,minNum=2.1)
fb.save()
fb = MyCalendar(user = 'moodade', moodDate = datetime(2016,11,17), moodid='1,2,3', color="purple",category="happy",maxNum=9.1,minNum=1.3)
fb.save()

