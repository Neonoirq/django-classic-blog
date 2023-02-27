from django.shortcuts import render
from django.http import HttpResponse


def posts(request):
    return HttpResponse('<h1>Testing the app</h1>')



