from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Reel


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'description']
        
class CreateReel(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ['title', 'reel', 'description']