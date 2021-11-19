from django import forms
from pictureApp.models import User_Post
from django.contrib.auth.models import User
from django.forms import widgets

fieldCSS = 'width: 300px; margin: 5px;'

class PostForm(forms.ModelForm):
    
    class Meta:
        model = User_Post
        fields =('image','tags')