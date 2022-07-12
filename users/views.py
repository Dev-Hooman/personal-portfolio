from mimetypes import init
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect 
# redirect helps to push back to url as arg
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#importing forms
from users.forms import RegistrationForm
from django.contrib import messages

from . models import userAccount
#------------------------------------------------------------

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "account/user.html")
        #homepage or maybe profile


def profile(request, slug):
    if request.user.is_authenticated:
        userInfo = userAccount.objects.filter(username=slug).first()
        context = {'userInfo' : userInfo}
        return render(request, 'account/profile.html', context)
    else:
        return redirect('home')


def logout_view(request):
    message_Display = None

    logout(request)
    message_Display = "Logged out!"
    messages.info(request, 'You Have Successfully Logged out')
    context = {'messageDisplay' : message_Display,}

    return render(request, 'home/index.html' , )

    
