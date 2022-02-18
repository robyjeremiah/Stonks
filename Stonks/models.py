from tokenize import group
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    #use_in_migrations = True

    def _create_user(self, email, password, dob, first_name, last_name,**extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        #email = self.normalize_email(email)
        user = self.model(email = self.normalize_email(email), 
                          dob = dob,
                          first_name = first_name,
                          last_name = last_name,
                          **extra_fields)     
        tempyear= str(dob.year)[2] + str(dob.year)[3]
        if dob.month >=10:
            user.username = str(first_name[0])+str(last_name)+str(dob.month)+tempyear
        else:
            user.username = str(first_name[0])+str(last_name)+"0"+str(dob.month)+tempyear
        user.set_password(password)
        user.save(using=self._db)
        print(user.username)
        print(user.dob)
        return user

    def create_user(self, email, password, dob, first_name, last_name,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, dob, first_name, last_name,**extra_fields)

    def create_superuser(self, email, password, dob, first_name, last_name,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, dob, first_name, last_name,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    address = models.CharField(_('address'), max_length=254, blank=True)
    dob = models.DateField(_('DateofBirth'),auto_now = False,blank = True, null = True)
    group = Group.objects.get(name="Administrator")
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name','dob']

# Security Questions stored in database
class SecurityQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.question
    class Meta:
        db_table = 'security_questions'

class SecurityAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    security_questions = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return self.answer
    class Meta:
        db_table = 'security_answers'
