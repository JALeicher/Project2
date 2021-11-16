from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
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

def signup_View(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
    
    return render(request, "picApp/signUp.html" )

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def userpage_view(request):
    return render(request,"picApp/userpage.html")