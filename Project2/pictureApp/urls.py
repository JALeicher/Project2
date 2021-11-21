from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("login",views.login_view, name="login"),
    path("signup",views.signup_request, name="signup"),
    path("logout", views.logout_view, name ="logout"),
    path("newpost",views.imageUpload_view, name="imageUpload"),
    path("userposts/<str:username>",views.userposts_view, name = "userPosts"),
    path("albums",views.albums_view,name="albums"),
    path("add_album",views.albumCreate_View,name="addAlbum"),
    path("albums/<str:albumName>",views.albumContent_View,name="viewAlbum"),
    path("homepage/", views.search_view , name="search"),
    path("homepage/<slug:slug>/", views.tagged_view, name="tagged"),
]
