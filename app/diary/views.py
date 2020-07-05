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
  category = request.POST['category']
  userName = request.POST['name']
  body = request.POST['article']
  # analysisBody = analysis.langAnalysis(body)
  params = {
    'category':category,
    'userName':userName,
    'body':body,
  }
  return render(request, 'diary/result.html', params)