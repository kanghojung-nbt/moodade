from django.shortcuts import render
from django.views.generic import ListView

from mood.models import Mood


# Create your views here.

# class MoodLV(ListView):
#     model = Mood

# def emoticon(request , emoticon):
#     mycolor=request.GET['emoticon']
#     template = loader.get_template('mood/mood_list.html')
#     mood_verb_list = Mood.objects.filter(mood_verb=mycolor)
#     context={'mood_verb_list': mood_verb_list}
#     return   HttpResponse(template.render(context))


class MoodLV(ListView):
    model = Mood


def mood_verb(request, pEmoticon):
    mymood = Mood.objects.filter(emotion=pEmoticon)
    context = {'mood_verb_list': mymood}
    return render(request, 'mood/mood_test.html', context)





