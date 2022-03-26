from dataclasses import fields
import queue
from .models import SecurityQuestion, User, Account
from .forms import CustomUserForm
from .decorators import allowed_users, unauthenticated_user
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# index -- Function used to handle logging in user and rendering login page


def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.groups.filter(name='Administrator'):
            login(request, user)
            print('Administrator Logged In!')
            return redirect('/adminHome/')
        elif user is not None and user.groups.filter(name='Accountant'):
            login(request, user)
            print('Accountant Logged In!')
            return redirect('/generalHome/')
        elif user is not None and user.groups.filter(name='Manager'):
            login(request, user)
            print('Manager Logged In!')
            return redirect('/generalHome/')
        else:
            messages.info(
                request, 'User OR Password is incorrect. Please Try Again.')
            return redirect('/')
    else:
        return render(request, 'login.html')

# loggedOut -- Function used to sign out a user


def loggedOut(request):
    print('Logged Out!')
    logout(request)
    return redirect('index')

# newUser -- Can be called to create a user specifically through the newUser template


def newUser(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = User.objects.latest('id')
            accountant = Group.objects.get(name='Accountant')
            accountant.user_set.add(new_user)
            messages.success(
                request, 'Account created successfully! Check your email for more information.')
            email = request.POST.get("email", None)
            try:
                subject = 'Complete Account Creation'
                message = 'Click on the following link in order to complete your account information:'
                send_mail(
                    subject,
                    message,
                    'automatedEmail@example.com',
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('newUser')
    else:
        form = CustomUserForm()

    return render(request, 'newUser.html', {'form': form})

# forgotPass -- Function used to current render the forgot password page


def forgotPass(request):
    return render(request, 'forgotPass.html')

# adminHome -- Function used to only allow Administrators (using decorators) to sign into this rendered template


@login_required(login_url='/')
@allowed_users(allowed_roles=['Administrator'])
def adminHome(request):
    user_list = User.objects.all()
    group_list = Group.objects.all()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = User.objects.latest('id')
            accountant = Group.objects.get(name=request.POST['role'])
            accountant.user_set.add(new_user)
            User.objects.filter(username=new_user).update(
                role=request.POST['role'])
            return redirect('adminHome')
    else:
        form = CustomUserForm()

    context = {
        'user_list': user_list,
        'group_list': group_list,
        'form': form,
    }

    return render(request, 'adminhome.html', context)

# delete_user -- Function that can be called to delete a user with providing the primary key of the users table


@login_required(login_url='/')
def delete_user(request, pk):
    username = User.objects.get(pk=pk).username
    b = User.objects.filter(username=username)
    b.delete()

    return redirect('adminHome')

# edit_user -- Function that can be used to get the information about an individual user


@login_required(login_url='/')
def edit_user(request):
    if request.method == "GET":
        user_id = request.GET.get("user_id", None)
        if User.objects.filter(id=user_id).exists():
            user = User.objects.all().filter(id=user_id)
            userInfo = serializers.serialize('json', user, fields=(
                'first_name',
                'last_name',
                'email',
                'role',
                'dob',
                'is_staff',
                'username'
            ))
            return JsonResponse({"valid": True, "user": userInfo}, status=200)
        else:
            return JsonResponse({"valid": False}, status=200)
    return JsonResponse({}, status=400)

# update_user -- Function that can be used to edit the information about the user


@login_required(login_url='/')
def update_user(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username", None)
            user = User.objects.get(username=username)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.role = request.POST['role']
            password = request.POST['password']
            confirmPassword = request.POST['confirmPassword']
            if password and confirmPassword and password != confirmPassword:
                print("Passwords did not match")
            else:
                user.set_password(password)
            group = Group.objects.get(name=request.POST['role'])
            group.user_set.add(user)
            is_staff = bool(request.POST['is_staff'])
            user.is_staff = is_staff
            user.save()
            return JsonResponse({'status': 'Success', 'msg': 'Saved successfully!'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})
    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})

    return render(request, 'updateProfileAdmin.html')


@login_required(login_url='/')
@allowed_users(allowed_roles=['Accountant', 'Manager'])
def generalHome(request):
    return render(request, 'generalHome.html')


def security(request):
    security_question_list = SecurityQuestion.objects.all()
    context = {
        'security_question_list': security_question_list,
    }
    return render(request, 'security.html', context)


def emailSent(request):
    return render(request, 'emailSent.html')


def passwordReset(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(queue(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Stonks Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(c)
                    try:
                        send_mail(subject, email, [
                                  user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/passwordConfirm/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='passwordReset.html', context={"password_reset_form": password_reset_form})


@login_required(login_url='/')
def passwordConfirm(request):
    return render(request, 'passwordConfirm.html')


@login_required(login_url='/')
def chartOfAccounts(request):
    Account_list = Account.objects.all()
    context = {
        'Account_list': Account_list,
    }
    return render(request, 'chartOfAccounts.html', context)

# Retrieves all the data for that specific account within the model


@login_required
def edit_account(request):
    if request.method == "GET":
        account_number = request.GET.get("account_number", None)
        if Account.objects.filter(account_number=account_number).exists():
            account = Account.objects.all().filter(account_number=account_number)
            account_info = serializers.serialize('json', account, fields=(
                'account_name',
                'account_category',
                'account_subcategory',
                'account_description',
                'initial_balance',
                'balance',
                'debit',
                'credit',
                'statement',
                'normal_side',
                'comment'
            ))

            return JsonResponse({"valid": True, "account": account_info}, status=200)
        else:
            return JsonResponse({"valid": False, "message": "Not able to retrieve data"}, status=200)

    return JsonResponse({}, status=400)


@login_required(login_url='/')
def useraccount(request):
    return render(request, 'useraccount.html')


@login_required(login_url='/')
def eventlog(request):
    Account_list = Account.objects.all()

    context = {
        'Account_list': Account_list,
    }
    return render(request, 'eventlog.html', context)


@login_required(login_url='/')
def listJournals(request):
    return render(request, 'ListOfJournals.html')


@login_required(login_url='/')
def addJounral(request):
    return render(request, 'addJournal.html')
