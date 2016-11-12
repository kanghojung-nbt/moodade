from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from moodcalendar.models import  *
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

def calendar(request):
    return render(request,'calendar/result.html',{})

#캘린더에서 요청하면 ajax 처리한다.

@csrf_protect
def ajaxCalendr(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.is_ajax():
        year =  int(request.POST.get('thisyear',False))
        month = int(request.POST.get('thismonth', False))
        lastday = int(request.POST.get('lastday', False))
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month, 30)


        mydata = MyCalendar.objects.filter(moodDate__range=(start_date, end_date), user=request.user)
        print (mydata)
        mydata= serializers.serialize('json', mydata)


        return JsonResponse(mydata,safe=False)

def mycalendar(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    calendarlist=MyCalendar.objects.all()
    if request.method == 'POST':  # 만약 폼 의해 제출
        idlist = request.POST.get('idlist', False)
        verbmin = request.POST.get('verbmin', False)
        verbmax = request.POST.get('verbmax', False)
        color= '%s' % request.POST.get('category', False)
        mycategory = '%s' % request.POST.get('category', False)
        MyCalendar.objects.create(user=request.user.username,  moodid=idlist, color=mycategory, category='angry',maxNum=verbmax, minNum=verbmin)
        context={'idlist':idlist,'verbmin':verbmin,'verbmax':verbmax,'mycategory':mycategory,'color':color,'calendarlist':calendarlist}
        print(calendarlist)
    return render(request, 'calendar/basic.html',{} )