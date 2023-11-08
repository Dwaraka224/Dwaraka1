from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dwaraka(request):
    return HttpResponse('hi mama')

def macha(request):
    return render(request,'macha.html')
