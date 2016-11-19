from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
from moodcalendar.models import  Memo,MyCalendar
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
        end_date = datetime(year, month, lastday)
        mydata = MyCalendar.objects.filter(moodDate__range=(start_date, end_date), user=request.user)
        mydata= serializers.serialize('json', mydata)
        return JsonResponse(mydata,safe=False)

def readMemo(request):              #날짜를 클릭했을때 메모를 보여준다.
    if request.is_ajax():
        myear = str(request.POST.get('year', False))
        mmonth = str(request.POST.get('month', False))
        mday = str(request.POST.get('day', False))
        date = myear + ':' + mmonth + ':' + mday
        data = Memo.objects.filter(
            user=request.user.username,
            moodDate=date
        )
        if data.exists():
            data= data[0].memo
        else:
            data = ""
        return HttpResponse(data)

def makeOrUpdateMemo(request):             #
    if request.is_ajax():
        myear = str(request.POST.get('year', False))
        mmonth = str(request.POST.get('month', False))
        mday = str(request.POST.get('day', False))
        memo = request.POST.get('memo', False)
        date = myear+':'+mmonth+':'+mday
        print(date)
        a = Memo.objects.filter(
            user=request.user.username,
            moodDate=date
        )
        if a.exists():
            k =Memo.objects.get(user=request.user.username, moodDate=date)
            k.memo=memo
            k.save()
        else:
            Memo.objects.create(user=request.user.username, memo=memo, moodDate=date)

        return HttpResponse(memo)




def mycalendar(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    calendarlist=MyCalendar.objects.all()
    if request.method == 'POST':  # 만약 폼 의해 제출
        idlist = request.POST.get('idlist', False)
        print(idlist)
        verbmin = request.POST.get('verbmin', False)
        verbmax = request.POST.get('verbmax', False)
        color= '%s' % request.POST.get('category', False)
        mycategory = '%s' % request.POST.get('category', False)
        MyCalendar.objects.create(user=request.user.username,  moodid=idlist, color=mycategory, category='angry',maxNum=verbmax, minNum=verbmin)
        context={'idlist':idlist,'verbmin':verbmin,'verbmax':verbmax,'mycategory':mycategory,'color':color,'calendarlist':calendarlist}

    return render(request, 'calendar/basic.html',{} )