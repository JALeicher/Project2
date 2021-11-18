from datetime import date
from django.http.response import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.contrib.auth import authenticate, get_user, login, logout
from django.urls import reverse

from pictureApp.forms.forms import SignUpForm, PostForm
from .models import *

# Create your views here.
def homepage_view(request):
    posts = User_Post.objects.order_by('-date')
    return render(request, "picApp/homepage.html",{'posts':posts})

def userposts_view(request, username):
    posts = User_Post.objects.filter(main_user_id= request.user).order_by('-date')
    return render(request, "picApp/homepage.html",{'posts':posts})

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
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.create_user(username=username,email=email,password=request.POST['password1'])
        user.save()
        return HttpResponseRedirect(reverse("login"))
        '''form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("login"))'''      
    else:
        return render(request, "picApp/signUp.html" ) 
    '''form = SignUpForm()
    return render(request=request, template_name="picApp/signUp.html",context={'signUpForm':form})'''

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