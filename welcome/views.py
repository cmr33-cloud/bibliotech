from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(req):
    return HttpResponse(f'<h1>Welcome to BiblioTech.</h1>')

def info(req):
    return HttpResponse(f'<h1>We hope you find what you need here.</h1>')