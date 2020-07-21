from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def rules(request):
  return render(request, 'rules/rule1.html')