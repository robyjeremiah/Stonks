from .models import SecurityQuestion, User
from .forms import CustomUserForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)
        if user is not None and user.groups.filter(name='Administrator'):
            login(request, user)
            print('Administrator Logged In!')
            return redirect('/adminHome/')
        elif user is not None and user.groups.filter(name='Accountant'):
            login(request, user)
            print('Accountant Logged In!')
            return redirect('/generalHome/')
        else:
            messages.info(request, 'User OR Password is incorrect. Please Try Again.')
            return redirect('/')
    else:
        return render(request, 'login.html')

def loggedOut(request):
    print('Logged Out!')
    logout(request)
    return redirect('index')

def newUser(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = User.objects.latest('id');
            accountant = Group.objects.get(name='Accountant')
            accountant.user_set.add(new_user)
            messages.success(request, 'Account created successfully!')
            return redirect('newUser')
    else:
        form = CustomUserForm()

    return render(request, 'newUser.html', {'form': form})

def forgotPass(request):
    return render(request, 'forgotPass.html')

@login_required(login_url='index')
def adminHome(request):
    return render(request, 'adminhome.html')

@login_required(login_url='login')
def generalHome(request):
    return render(request, 'generalHome.html')

def security(request):
    security_question_list = SecurityQuestion.objects.all()
    context = {
        'security_question_list': security_question_list
    }
    return render(request, 'security.html', context)

def emailSent(request):
    return render(request, 'emailSent.html')

def passwordReset(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Stonks Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(c)
                    try:
                        send_mail(subject, email, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/passwordConfirm/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='passwordReset.html', context={"password_reset_form":password_reset_form})

def passwordConfirm(request):
    return render(request, 'passwordConfirm.html')