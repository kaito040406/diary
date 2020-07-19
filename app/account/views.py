from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import idForm
from .forms import passForm
from .forms import passForm_a
from .models import job_t_user
from .lib import random
from datetime import datetime


# Create your views here.

def registration(request):
  idDate = idForm()
  passDate = passForm()
  idError = ""
  passError1 = ""
  passError2 = ""
  params={
    'idForm':idDate,
    'passForm':passDate,
    'idError':idError,
    'passError1':passError1,
    'passError2':passError2
  }
  return render(request, 'account/registration.html',params)

def registrationResult(request):
  if request.method == 'POST':
    username = idForm(request.POST)
    password1 = passForm(request.POST)
    password2 = passForm_a(request.POST)
    email = random.randomname(15) + "@example.com"
    if password1 == password2:
      if username.is_valid and password1.is_valid:
        user = User.objects.create_user(username, email, password=password1)
        user_id = User.objects.get(email=email)
        profile = job_t_user(user_id = user_id.id,admin_level = 1, del_flg = 0, user_name = "ピカピカの新入生", user_create_day = datetime.now())
        profile.save()
        return HttpResponse("成功です")
      else:
        return HttpResponse("ルール外")
    else:
      return HttpResponse("パスワードが違う")
    



def login(request):
  return render(request, 'account/login.html')

