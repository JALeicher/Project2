from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from taggit.models import Tag

from pictureApp.forms.forms import PostForm
from .forms import *
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
    else:
        return render(request, "picApp/signUp.html" ) 

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def userpage_view(request):
    return render(request,"picApp/userpage.html")

def imageUpload_view(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,user_pk=request.user.pk,)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.main_user=request.user 
            newpost.save()
            form.save_m2m()
        return HttpResponseRedirect(reverse("homepage"))
    else:
       return render(request, "picApp/imageUpload.html",{"form":PostForm(user_pk=request.user.pk)} ) 