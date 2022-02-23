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

class AccountQuerySet(models.QuerySet):
    def Assets(self):
        return self.filter(role='A')

    def Liabilities(self):
        return self.filter(role='L')
    
    def EquityAccounts(self):
        return self.filter(role='EA')
    def Revenues(self):
        return self.filter(role='R')
    def Expenses(self):
        return self.filter(role='E')
    def Other(self):
        return self.filter(role='O')

class ChartOfAccounts(models.Manager):
    
    def create_account(self, account_name, account_category,account_description,**extra_fields):
        account = self.model(account_name = account_name, 
                          account_category = account_category,
                          account_description = account_description,
                          **extra_fields)
        if account_category == 'Assets':
            count = Account.objects.filter(account_category='Assets').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statement = "Balance sheet"
            account.normal_side = "Left"
            
            account.statement.Statement.BS
        elif account_category == 'Liabilities':
            count = Account.objects.filter(account_category='Liabilities').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statement = "Balance sheet"
            account.normal_side = "Right"
        elif account_category == 'Equity Accounts':
            count = Account.objects.filter(account_category='Equity Accounts').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statementc
            account.statement = "Balance sheet"
            account.normal_side = "Right"
        elif account_category == 'Revenues':
            count = Account.objects.filter(account_category='Revenues').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statement = "Income statement"
            account.normal_side = "Right"
        elif account_category == 'Expenses':
            count = Account.objects.filter(account_category='Expenses').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statement = "Income statement"
            account.normal_side = "Left"
        elif account_category == 'Other':
            count = Account.objects.filter(account_category='Other').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            account.account_number = temp
            account.statement = "Cash flow statement"
        account.save(using=self._db)
        return account
    
    
    pass

class Account(models.Model):
    # ATP this point some of this is just notes for me
    
    StatementChoices = (
    ("BS", "Balance sheet"),
    ("IS", "Income statement"),
    ("CFS", "Cash flow statement"),)
    
    Account_Category= (
    ("A", "Assets"),
    ("L", "Liabilities"),
    ("EQ", "Equity Accounts"),
    ("R", "Revenues"),
    ("EX", "Expenses"),
    ("O", "Other"),)
    
    # Account_Number = (
    # ("Assets", "100"),
    # ("Liabilities", "200"),
    # ("Equity Accounts", "300"),
    # ("Revenues", "400"),
    # ("Expenses", "500"),
    # ("Other", "600"),
    # )
    
    # Dont know what this iis
    userid =  models.IntegerField(_('User id'), blank=True)
    
    id = models.BigAutoField(primary_key=True)
    account_name =  models.CharField(_('Account Name'), max_length=30, unique = True)
    account_number =  models.IntegerField(_('Account Number'), blank=True)
    account_description =  models.CharField(_('Account Description'), max_length=300, blank=True)
    account_category =  models.CharField(_('Account Category'), max_length=30, choices = Account_Category, blank = False)
    account_subcategory =  models.CharField(_('Account Subcategory'), max_length=30, blank=True)
    
    normal_side =  models.CharField(_('Normal Side'), max_length=5, blank=True)
    Date_time_added =  models.DateTimeField(_('Date/Time Added'), max_length=30, blank=True,auto_now=True)
    Comment =  models.CharField(_('username'), max_length=300, blank=True)
    
    initial_balance =  models.DecimalField(_('initial balance'), max_length=30, blank=True, decimal_places = 2, max_digits=17)
    debit =  models.DecimalField(_('debit'), max_length=30, blank=True, decimal_places = 2, max_digits=17)
    credit =  models.DecimalField(_('credit'), max_length=30, blank=True, decimal_places = 2, max_digits=17)
    balance =  models.DecimalField(_('balance'), max_length=30, blank=True, decimal_places = 2, max_digits=17)
    order =  models.IntegerField(_('Order'), blank=True)
    statement =  models.CharField(_('Financial Statement'), max_length=30, choices = StatementChoices, blank=True)
    
    objects = ChartOfAccounts()
    
    

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
