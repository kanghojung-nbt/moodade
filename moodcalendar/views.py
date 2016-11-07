from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect



def mycalendar(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'calendar/basic.html', {})
