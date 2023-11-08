from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def dwaraka(request):
    return HttpResponse('<h1><marquee>Hi Mama how are you</h1></marquee>')

def basha(request):
    return HttpResponse('<h1><marquee>Fine mama how about you</marquee></h1>')
