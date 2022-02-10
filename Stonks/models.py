from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    username = models.CharField(_('username'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    address = models.CharField(_('address'), max_length=254, blank=True)
    dob = models.DateField(_('DateofBirth'),auto_now = False,blank = True, null = True)
    #avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','dob']

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
