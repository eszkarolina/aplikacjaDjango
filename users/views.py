from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


def test(request):
    return HttpResponse('users!')


def create(request):
	if request.method =="GET":
		form = UserCreationForm()

		return render(request, 'users/create.html', {'form1': form})

	elif request.method =="POST":
		new_user=User()
		form = UserCreationForm(request.POST, instance=new_user)
		if form.is_valid():
			new_user=form.save(commit=False)
			new_user.is_active=False
			new_user.save()
			return redirect("users:new")

	else:
		return HttpResponse("akuku")		

def activate(request, key):

	profile=Profile.objects.get(secret=key)
	user=profile.user
	user.is_active=True
	user.save()
		


	return render(request, 'users/activate.html', {})