from typing import re

from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .form import SignupForm

def registerView(request):
    """signup
    to register users
    """
    if request.method == "POST":
        print("post가입")
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email=signupform.cleaned_data['email']
            user.nickName= signupform.cleaned_data['nickName']
            user.save()
            return HttpResponseRedirect(reverse("signup_ok"))
    elif request.method == "GET":
        signupform = SignupForm(request.POST)
    return render(request, "registration/register.html", {
        "signupform": signupform,
    })

def my_view(request):
    username = request.POST['username']
    password = request.POST['username']
    user = authenticate(username=username , password=password)
    if user is not None:
        login(request,user)



# --- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

#
# # --- User Creation
# class UserCreateView(CreateView):
#     template_name = 'registration/register.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('register_done')
#
#
# class UserCreateDoneTV(TemplateView):
#     template_name = 'registration/register_done.html'
#
#
# # --- @login_required
# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)
