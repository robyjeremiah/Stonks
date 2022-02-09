from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserForm
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)
        if user is not None:
            return render(request, 'security.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    #return render(request, 'login.html')

def newUser(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = CustomUserForm()

    return render(request, 'newUser.html', {'form': form})
    #return render(request, 'newUser.html')

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