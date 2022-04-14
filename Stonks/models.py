from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    #use_in_migrations = True

    def _create_user(self, email, password, dob, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        admin_group = Group.objects.get(name="Administrator")
        user = self.model(email=self.normalize_email(email),
                          dob=dob,
                          first_name=first_name,
                          last_name=last_name,
                          **extra_fields)
        tempyear = str(dob.year)[2] + str(dob.year)[3]
        if dob.month >= 10:
            user.username = str(first_name[0]) + \
                str(last_name)+str(dob.month)+tempyear
        else:
            user.username = str(
                first_name[0])+str(last_name)+"0"+str(dob.month)+tempyear
        user.set_password(password)
        user.save(using=self._db)
        admin_group.user_set.add(user)
        print(user.username)
        print(user.dob)
        return user

    def create_user(self, email, password, dob, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'Manager')
        return self._create_user(email, password, dob, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, dob, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Administrator')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, dob, first_name, last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), max_length=30, unique=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    address = models.CharField(_('address'), max_length=254, blank=True)
    dob = models.DateField(
        _('DateofBirth'), auto_now=False, blank=True, null=True)
    role = models.CharField(_('role'), max_length=50, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'dob']


class AccountQuerySet(models.QuerySet):
    def Assets(self):
        return self.filter(account_category='A')

    def Liabilities(self):
        return self.filter(account_category='L')

    def EquityAccounts(self):
        return self.filter(account_category='EQ')

    def Revenues(self):
        return self.filter(account_category='R')

    def Expenses(self):
        return self.filter(account_category='EX')

    def Other(self):
        return self.filter(account_category='O')


class AccountManager(models.Manager):

    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    def Assets(self):
        return self.get_queryset().Assets()

    def Liabilities(self):
        return self.get_queryset().Liabilities()

    def EquityAccounts(self):
        return self.get_queryset().EquityAccounts()

    def Revenues(self):
        return self.get_queryset().Revenues()

    def Expenses(self):
        return self.get_queryset().Expenses()

    def Other(self):
        return self.get_queryset().Other()

    def CopyCheck(tempaccount, **extra_fields):
        tempaccount.account_number
        if tempaccount == NULL:
            raise ValueError('Didnt recieve Temp')
        if tempaccount.account_number == NULL:
            raise ValueError('Didnt recieve account number')
        if Account.objects.filter(account_number=tempaccount.account_number).exists():
            return True
        else:
            return False


class Account(models.Model):
    # ATP this point some of this is just notes for me

    StatementChoices = (
        ("BS", "Balance sheet"),
        ("IS", "Income statement"),
        ("RE", "Retained Earnings statement"),
    )

    Account_Category = (
        ("A", "Assets"),
        ("L", "Liabilities"),
        ("EQ", "Equity Accounts"),
        ("R", "Revenues"),
        ("EX", "Expenses"),
        ("O", "Other"),
    )

    # id = models.BigAutoField(primary_key=True)
    account_name = models.CharField(
        _('Account Name'), max_length=30, unique=True)
    account_number = models.IntegerField(
        _('Account Number'), blank=True, primary_key=True)
    account_description = models.CharField(
        _('Account Description'), max_length=300, blank=True)
    account_category = models.CharField(
        _('Account Category'), max_length=30, choices=Account_Category, blank=False)
    account_subcategory = models.CharField(
        _('Account Subcategory'), max_length=30, blank=True)

    balance = models.DecimalField(
        _('Balance'), blank=True, decimal_places=2, max_digits=17, null=True)
    initial_balance = models.DecimalField(
        _('Initial balance'), blank=True, decimal_places=2, max_digits=17, null=True)
    debit = models.DecimalField(
        _('Debit'), blank=True, decimal_places=2, max_digits=17, null=True)
    credit = models.DecimalField(
        _('Credit'), blank=True, decimal_places=2, max_digits=17, null=True)
    order = models.IntegerField(_('Order'), blank=True, null=True)
    statement = models.CharField(
        _('Financial Statement'), max_length=30, choices=StatementChoices, blank=True, null=True)

    # Dont know what this iis
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    normal_side = models.CharField(_('Normal Side'), max_length=8, blank=True)
    date_time_added = models.DateField(
        _('Date/Time Added'), max_length=30, blank=True, auto_now=True)
    comment = models.CharField(_('Comment'), max_length=300, blank=True)

    objects = AccountManager()

    def save(self, *args, **kwargs):
        if self.account_category == 'A':
            count = Account.objects.filter(account_category='A').count()
            count = count + 1
            temp = str(100) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(100) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "BS"
            self.normal_side = "Debit"
        elif self.account_category == 'L':
            count = Account.objects.filter(account_category='L').count()
            count = count + 1
            temp = str(200) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(200) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "BS"
            self.normal_side = "Credit"
        elif self.account_category == 'EQ':
            count = Account.objects.filter(account_category='EQ').count()
            count = count + 1
            temp = str(300) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(300) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "BS"
            self.normal_side = "Credit"
        elif self.account_category == 'R':
            count = Account.objects.filter(account_category='R').count()
            count = count + 1
            temp = str(400) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(400) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "IS"
            self.normal_side = "Credit"
        elif self.account_category == 'EX':
            count = Account.objects.filter(account_category='EX').count()
            count = count + 1
            temp = str(500) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(500) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "IS"
            self.normal_side = "Debit"
        elif self.account_category == 'O':
            count = Account.objects.filter(account_category='O').count()
            count = count + 1
            temp = str(600) + str(count)
            temp = int(temp)
            copycheck = True
            judge = False
            while copycheck == True:
                judge = Account.objects.filter(
                    account_number=self.account_number).exists()
                if (judge == False):
                    copycheck = False
                    break
                elif (judge == True):
                    count = count + 1
                    temp = str(600) + str(count)
                    temp = int(temp)
                    copycheck = True
            self.account_number = temp
            self.statement = "RE"

        super(Account, self).save(*args, **kwargs)


class Journal(models.Model):
    Journal_Categories = (
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    )

    journal_id = models.AutoField(primary_key=True)
    date_time_added = models.DateField(
        _('Date/Time Added'), max_length=30, blank=True, auto_now=True)
    description = models.CharField(
        _('Description of Entry'), max_length=300, blank=True)
    journal_status = models.CharField(
        _('Journal Status'), max_length=30, choices=Journal_Categories, null=True)
    balance = models.DecimalField(
        _('Balance'), blank=True, decimal_places=2, max_digits=17, null=True)
    pass


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        _('Transaction Description'), max_length=300, blank=True)
    amount = models.DecimalField(
        _('Amount'), blank=True, decimal_places=2, max_digits=17, null=True)
    transaction_type = models.BooleanField(_('Transaction Type'))

    pass


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(
        _("Date/Time"), auto_now=False, auto_now_add=False, blank=True)
    date_updated = models.DateTimeField(
        _("Date/Time"), auto_now=False, auto_now_add=False, blank=True)
    file_name = models.CharField(_("File Name"), max_length=500)
    user = models.ForeignKey(User, verbose_name=_(
        "User"), on_delete=models.CASCADE)
    journal_entry = models.ForeignKey(Journal, verbose_name=_(
        "Journal Entry"), on_delete=models.CASCADE)

    pass

# Security Questions stored in database


class SecurityQuestion(models.Model):
    question = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'security_questions'


class SecurityAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    security_questions = models.ForeignKey(
        SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'security_answers'
