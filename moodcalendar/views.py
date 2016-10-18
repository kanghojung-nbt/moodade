from django.shortcuts import render




def mycalendar(request):
    return render(request, 'calendar/basic.html', {})
