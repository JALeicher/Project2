from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("login",views.login_view, name="login"),
    path("signup",views.signup_request, name="signup"),
    path("logout", views.logout_view, name ="logout"),
    path("user",views.userpage_view, name="userpage"),
    path("newpost",views.imageUpload_view, name="imageUpload"),
    path("userposts/<str:username>",views.userposts_view, name = "userPosts")
]
