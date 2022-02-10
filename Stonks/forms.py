from urllib.request import DataHandler
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
#https://dev.to/yahaya_hk/usercreation-form-with-multiple-fields-in-django-ek9


class CustomUserForm(UserCreationForm):
    #username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    #password1 = forms.CharField()
    #password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ('email','first_name','last_name','dob','password1' ,'password2')
        
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
        #user.set_password(user.password1)
        user.save()