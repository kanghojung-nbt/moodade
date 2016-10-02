from django.shortcuts import render

from django.views.generic import ListView, DetailView
from mood.models import Mood

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class MoodkLV(ListView):
    model = Mood


