from django import forms
from .models import Post,Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)


class categoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields=('title' , 'text',)

