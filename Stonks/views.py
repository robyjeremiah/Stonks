from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the Home Page!')

def profile(request):
    return HttpResponse('Welcome to the Profile Page!')

def test(request):
    return HttpResponse('Welcome to the Test Page!')

def login(request):
    return render(request, 'login.html')