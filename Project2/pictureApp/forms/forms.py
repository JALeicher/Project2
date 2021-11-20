from django import forms
from django.forms import fields
from pictureApp.models import User_Albums, User_Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    def __init__(self,*args,user_pk=None, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['shared_users'].queryset = User.objects.exclude(pk=user_pk)
    
    class Meta:
        model = User_Post
        fields =['image','tags','shared_users']
        shared_users=forms.ModelMultipleChoiceField(
        queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    
    
    
class AlbumForm(forms.ModelForm):
    
    def __init__(self,user_pk=None,*args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['contents'].queryset = User_Post.objects.filter(main_user_id = user_pk)
    
    class Meta:
        model = User_Albums
        fields=['album_name','albumDescription','contents']
        contents=forms.ModelMultipleChoiceField(
        queryset=User_Post.objects.all(), widget=forms.CheckboxSelectMultiple
    )