from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the Home Page!')

def profile(request):
    return HttpResponse('Welcome to the Profile Page!')

def test(request):
    return HttpResponse('Welcome to the Test Page!')

def login(request):
    return HttpResponse(loader.get_template('Stonks\login.html'))