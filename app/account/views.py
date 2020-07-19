from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
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
  if request.user.is_authenticated:
    return HttpResponse("ログイン済み")
  else:
    if 'accountid' in request.session and 'pass' in request.session and 'pass_a' in request.session:
      idDateError = request.session['accountid']
      passError = request.session['pass']
      passErrorA = request.session['pass_a']
      idError = request.session['idError']
      passError1 = request.session['passError']
      del request.session['accountid']
      del request.session['pass']
      del request.session['pass_a']
      del request.session['idError']
      del request.session['passError']
      idDate = idForm({'idForm':idDateError})
      # idDate = idForm({'idForm':idDateError})
      passDate = passForm({'passForm':passError})
      passDateA = passForm_a({'value':passErrorA})
      # passMessage = passForm({'passForm':passError})
    else:
      idError = ""
      passError1 = ""
      idDate = idForm()
      passDate = passForm()
      passMessage = ""
    passDateA = passForm_a()
    pass_passAError = ''
    passError2 = ""
    accountCheck = ""
    if 'pass_passA' in request.session:
      idDateError = request.session['accountid']
      pass_passAError = request.session['pass_passA']
      del request.session['accountid']
      del request.session['pass_passA']
      idDate = idForm({'idForm':idDateError})
    if 'accountid' in request.session:
      idDateError = request.session['accountid']
      accountCheck = request.session['accountExist']
      del request.session['accountid']
      del request.session['accountExist']
      idDate = idForm({'idForm':idDateError})
    params={
      'idForm':idDate,
      'passForm':passDate,
      'passForm_a':passDateA,
      'idError':idError,
      'passError1':passError1,
      'passError2':passError2,
      'pass_passAError':pass_passAError,
      'accountCheck':accountCheck

    }
    return render(request, 'account/registration.html',params)

def registrationResult(request):
  if request.user.is_authenticated:
    return HttpResponse("ログイン済み")
  else:
    if request.method == 'POST':
      username = request.POST['idForm']
      password1 = request.POST['passForm']
      password2 = request.POST['passForm_a']
      # return HttpResponse(password2)
      email = random.randomname(15) + "@example.com"
      if password1 == password2:
        if idForm(request.POST).is_valid() and passForm(request.POST).is_valid():
          if User.objects.filter(username=username).exists():
            checkProfile = job_t_user.objects.get(user_id_id=User.objects.get(username=username).id)
            if checkProfile.del_flg == 0:
              request.session['accountid'] = username
              request.session['accountExist'] = "このIDは既に使用されています"
              return redirect(to='/account/registration')
            elif checkProfile.del_flg == 1:
              user = User.objects.get(username=username)
              user.username = str(user.id) + str(random.randomname(30))
              user.save()
            else:
              return HttpResponse("システムエラー")
          user = User.objects.create_user(username, email, password=password1)
          authuser_id = User.objects.get(email=email)
          profile = job_t_user(user_id = authuser_id,admin_level = 1, del_flg = 0, user_name = "ピカピカの新入生", user_create_day = datetime.now(), user_updata_day = datetime.now())
          profile.save()
          return HttpResponse("成功です")
        else:
          request.session['accountid'] = username
          request.session['pass'] = password1
          request.session['pass_a'] = password2
          request.session['idError'] = idForm(request.POST).errors
          request.session['passError'] = passForm(request.POST).errors
          return redirect(to='/account/registration')
      else:
        request.session['accountid'] = username
        request.session['pass_passA'] = "入力したパスワードが違います"
        return redirect(to='/account/registration')
    



def login(request):
  if request.user.is_authenticated:
    return HttpResponse("ログイン済み")
  else:
    if 'errormessage' in request.session:
      errorMessage = request.session['errormessage']
      del request.session['errormessage']
    else:
      errorMessage = ''
    idDate = idForm()
    passDate = passForm()
    params={
      'idForm':idDate,
      'passForm':passForm,
      'errorMessage':errorMessage
    }
    return render(request, 'account/login.html',params)


def loginResult(request):
  if request.user.is_authenticated:
    return HttpResponse("ログイン済み")
  else:
    # if request.method == 'POST':
      username = request.POST['idForm']
      password = request.POST['passForm']
      if idForm(request.POST).is_valid() and passForm(request.POST).is_valid():
        user = authenticate(request, username=username, password=password)
        if user is not None:
          user = User.objects.get(username=username)
          login(request, user)
          return redirect(to='/diary')
        else:
          request.session['errormessage'] = "IDかパスワードをご確認ください"
          return redirect(to='/account/login')
      else:
        request.session['errormessage'] = "IDかパスワードをご確認ください"
        return redirect(to='/account/login')
    # return HttpResponse("aa")