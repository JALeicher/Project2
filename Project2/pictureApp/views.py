from datetime import date
from django.http.response import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from pictureApp.forms.forms import SignUpForm, PostForm
from .models import *

# Create your views here.
def homepage_view(request):
    return render(request, "picApp/homepage.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "picApp/login.html" )
    else:
        return render(request, "picApp/login.html" )

def signup_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("login"))
    form = SignUpForm()
    return render(request=request, template_name="picApp/signUp.html",context={'signUpForm':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def userpage_view(request):
    return render(request,"picApp/userpage.html")

def imageUpload_view(request):
    if request.method == "POST" and request.FILES['upload']:
        user = request.user
        im = request.FILES['upload']
        d = date.today()
        newpost = User_Post(main_user=user, image=im, date=d)
        newpost.save()
        return HttpResponseRedirect(reverse("homepage"))
    else:
       return render(request, "picApp/imageUpload.html" ) 