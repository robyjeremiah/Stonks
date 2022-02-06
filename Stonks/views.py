from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages

# Create your views here.
def index(request):
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
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Stonks/password/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Stonks Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    
                    return redirect("/passwordConfirm/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name='passwordReset.html', context={"password_reset_form":password_reset_form})

def passwordConfirm(request):
    return render(request, 'passwordConfirm.html')