from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserChangeForm
from .forms  import RegistrationForm,EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_redirect(request):
	return redirect("/accounts/login")

def register(request):
	if request.method=='POST':
		# form=UserCreationForm(request.POST)
		form=RegistrationForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/accounts/')
	else:
		# form=UserCreationForm()
		form=RegistrationForm()
		args={'form':form}
		return render(request,"accounts/reg_form.html",args)


def profile(request,pk=None):
	if pk:
		user=User.objects.get(pk=pk)
	else:
		user=request.user
	print(user)
	args={'user':user}
	return render(request,"accounts/profile.html",args)



def edit_profile(request):
	if request.method=='POST':
		# form=UserChangeForm(request.POST,instance=request.user)
		form=EditProfileForm(request.POST,instance=request.user)
		
		if form.is_valid:
			form.save()
			return redirect('/accounts/profile')
	else:
		# form=UserChangeForm(instance=request.user)
		form=EditProfileForm(instance=request.user)
		args={'form':form}
		return render(request,"accounts/edit_profile.html",args)

def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/accounts/profile')
		else:
			return redirect('/accounts/change_password')
	else:
		form=PasswordChangeForm(user=request.user)
		args={'form':form}
		return render(request,"accounts/change_password.html",args)
