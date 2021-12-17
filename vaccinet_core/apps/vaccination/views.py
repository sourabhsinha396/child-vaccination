from django.shortcuts import render
from django.http import HttpResponse


def ping(request):
    return HttpResponse('pong')


def homepage(request):
    return render(request, 'vaccination/homepage.html')