from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
#https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9


class CustomUserForm(UserCreationForm):
    #username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    #password1 = forms.CharField()
    #password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1' ,'password2' )