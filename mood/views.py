from django.shortcuts import render
from django.views.generic import ListView
from mood.models import Mood,DownText
from mood.forms import *
from django.views.generic.edit import FormView



def mood_verb(request, pEmoticon):
    mymood = Mood.objects.filter(emotion=pEmoticon).order_by('?')[0:20]
    context = {'mood_verb_list': mymood}
    return render(request, 'mood/mood_select.html', context)

def mood_select(request):
    return render(request, 'mood/select_emoticon.html', {})

def mood_form(request):
    if request.method == 'POST':  # 만약 폼 의해 제출
        k=(request.POST.get('verblist', False))
        verblist ='%s' %request.POST.get('verblist',False)
        print(k);
        print(verblist)
        splitedverb=verblist.split(",")
        returndata=[]
        for idx, val in enumerate(splitedverb):
            if(val!=''):
                returndata.append(int(val))
        mymood= Mood.objects.filter(id__in=returndata)

        context = {'myverb':mymood, 'category': mymood[0].color,'emoticon':mymood[0].emotion}
        # Mood.objects.filter(mood_Verb=)
        return  render(request, 'mood/result.html', context)


def mood_down(request):
    idlist =request.POST.get('idlist',False)
    verbmin=request.POST.get('verbmin',False)
    verbmax = request.POST.get('verbmax', False)
    mycategory ='%s' %request.POST.get('category',False)

    print(idlist)
    print(mycategory)
    downtext = DownText.objects.filter(category=mycategory) #다운받을 글귀
    context={'verbmin':verbmin,'verbmax':verbmax,'category':mycategory,'text':downtext}
    return render(request, 'mood/mood_download.html', context)



def moodverb_save_page(request):
    if request.method=='POST':
        myform=moodverb_save_page(request.POST)
    myform = moodverb_save_page(request.POST)
    context = {'my_mood_list':myform}
    return render(request,'result.html',context)



class verbFormView(FormView):
    form_class = moodverb_save_page
    template_name = "mood/result.html"
    def form_valid(self, form):
        verblist='%s' %self.request.POST['verblist']
        context ={}
        context['form'] = form
        context['verblist']=verblist
        return render(self.request, self.template_name, context)






