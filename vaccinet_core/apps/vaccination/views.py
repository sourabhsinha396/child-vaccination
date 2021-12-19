from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm


def ping(request):
    return HttpResponse('pong')


def homepage(request):
    return render(request, 'vaccination/homepage.html')


def contact_us(request):
    messages.success(request, "Your message was succesfully submitted.")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    return render(request, 'vaccination/contact_us.html')