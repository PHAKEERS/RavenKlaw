from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def new(request):
    return render(request, 'new.html')


def python(request):
    return render(request, 'python.html')
