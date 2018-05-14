from django import forms
from .models import Post

#unbound form
# class HomeForm(forms.Form):
# 	post=forms.CharField()

#bound with model form
class HomeForm(forms.ModelForm):
	post=forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':"What's on your mind ?"
		}))
	class Meta:
		model=Post
		fields={'post'}
