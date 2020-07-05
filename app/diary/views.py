from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
# from diary.lib import analysis

# Create your views here.
def index(request):
  return render(request, 'diary/index.html')

def show(request):
  return render(request, 'diary/show.html')

def create(request):
  return render(request, 'diary/create.html')


def form(request):
  userName = request.POST['userName']
  body = request.POST['body']
  # analysisBody = analysis.langAnalysis(body)
  params = {
    'userName':userName,
    'bodys':body,
  }
  return render(request, 'diary/result.html', params)