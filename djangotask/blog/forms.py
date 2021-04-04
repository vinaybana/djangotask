from django import forms
from .models import *
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)


class categoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields=('title' , 'text',)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('user', 'name', 'address', 'position',)

    def __init__(self, user, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(user=user)
