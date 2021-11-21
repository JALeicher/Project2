from django.db.models.query import EmptyQuerySet
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.models import Tag
import piexif


from pictureApp.forms.forms import PostForm, AlbumForm
from .models import *

# Create your views here.
def homepage_view(request):
    posts = User_Post.objects.order_by('-date')
    return render(request, "picApp/homepage.html",{'posts':posts})
    

def userposts_view(request):
    posts = User_Post.objects.filter(main_user_id= request.user).order_by('-date')
    message = "{}"
    return render(request, "picApp/userImages.html",{'posts':posts, 'message':message.format(request.user.username)})

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

def imageUpload_view(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,user_pk=request.user.pk)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.main_user=request.user 
            newpost.save()
            form.save_m2m()
        return HttpResponseRedirect(reverse("homepage"))
    else:
       return render(request, "picApp/imageUpload.html",{
           "form":PostForm(user_pk=request.user.pk)
        } )
   
def albums_view(request):
    albums = User_Albums.objects.filter(creator_id= request.user)
    return render(request,"picApp/albums.html",{'albums':albums}) 

def albumContent_View(request, albumName):
    album = User_Albums.objects.get(album_name=albumName)
    posts = album.contents.all()
    message = "{}/{}"
    return render(request, "picApp/userImages.html",{'posts':posts, 'message':message.format(request.user.username,albumName)})

def albumCreate_View(request):
    if request.method == "POST":
        form = AlbumForm(user_pk=request.user.pk ,data=request.POST)
        if form.is_valid():
            newAlbum = form.save()
            newAlbum.creator = request.user
            newAlbum.save()
        return HttpResponseRedirect(reverse("albums"))  
    else:
        return render(request,"picApp/albumsAdd.html",{
            'form': AlbumForm(user_pk=request.user.pk)          
        })
        
def search_view(request):
    print(request.GET.get('search'))
    posts = User_Post.objects.filter(tags__name__in=[request.GET.get('search')])
    context = {
        'posts':posts,
    }
    return render(request, 'picApp/homepage.html', context)
 
        
        
def tagged_view(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = User_Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'picApp/homepage.html', context)
        
        
'''def showMeta_view(request, post_id):
    selected=User_Post.objects.get(pk = post_id)
    image_name = str(selected)
    meta_dict = piexif.load(image_name)'''
        