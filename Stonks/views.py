from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the Home Page!')

def profile(request):
    return HttpResponse('Welcome to the Profile Page! Bubble butt')

def test(request):
    return HttpResponse('Welcome to the Test Page!')

def login(request):
    return render(request, 'login.html')

def newUser(request):
    return render(request, 'newUser.html')

def forgotPass(request):
    return render(request, 'forgotPass.html')

def security(request):
    return render(request, 'security.html')

def emailSent(request):
    return render(request, 'emailSent.html')

def passwordReset(request):
    return render(request, 'passwordReset.html')

def passwordConfirm(request):
    return render(request, 'passwordConfirm.html')