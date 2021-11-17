from django import forms
from pictureApp.models import User_Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

fieldCSS = 'width: 300px; margin: 5px;'

class SignUpForm(UserCreationForm): 
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder' :'something@somewhere.foo', 'style' : fieldCSS}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        widgets = {
            'username': forms.TextInput(attrs={'style' : fieldCSS}),
            'password1': forms.TextInput(attrs={'style' : fieldCSS}),
        }      
        
    def save(self, commit: bool = True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = User_Post
        fields =('image',)