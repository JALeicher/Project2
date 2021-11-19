from django import forms
from pictureApp.models import User_Post
from django.contrib.auth.models import User

fieldCSS = 'width: 300px; margin: 5px;'

class PostForm(forms.ModelForm):
    def __init__(self,user_pk=None,*args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['shared_users'].queryset =User.objects.exclude(pk=user_pk)
    
    class Meta:
        model = User_Post
        fields =['image','tags','shared_users']
        shared_users=forms.ModelMultipleChoiceField(
        queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    
    def __init__(self,user_pk=None,*args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['shared_users'].queryset =User.objects.exclude(pk=user_pk)
    
        