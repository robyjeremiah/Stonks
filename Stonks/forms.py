from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9


class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'id': 'fname'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'id': 'lname'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'id': 'email'}))
    dob = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'yyyy-mm-dd', 'id': 'date'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password', 'id': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'id': 'confirmPassword'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'dob')
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self):
        data = self.cleaned_data
        user = User(email=data['email'], 
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        dob= data['dob'],)
        if(str(data['password1']) == str(data['password2'])):
            user.set_password(data['password1'])
        tempyear= str(user.dob.year)[2] + str(user.dob.year)[3]
        if user.dob.month >=10:
            user.username = str(user.first_name[0])+str(user.last_name)+str(user.dob.month)+tempyear
        else:
            user.username = str(user.first_name[0])+str(user.last_name)+"0"+str(user.dob.month)+tempyear
        
        user.save()

