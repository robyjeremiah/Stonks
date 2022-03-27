from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Login Urls
    path('', views.index, name='index'),
    path('generalHome/', views.generalHome, name='userHome'),
    path('logout/', views.loggedOut, name='loggedOut'),
    # Create User Urls
    path('newUser/', views.newUser, name='newUser'),
    # Forgot Password Urls
    path('security/', views.security, name='security'),
    path('passwordConfirm/', views.passwordConfirm, name='passwordConfirm'),
    # Administrator Home Urls
    path('adminHome/', views.adminHome, name='adminHome'),
    path('adminHome/delete/<pk>', views.delete_user, name='delete_user'),
    path('adminHome/edit/', views.edit_user, name='edit_user'),
    path('adminHome/update/', views.update_user, name='update_user'),
    # Chart of Accounts Urls
    path('chartOfAccounts/', views.chartOfAccounts, name='chartOfAccounts'),
    path('chartOfAccounts/viewAccountInfo/',
         views.useraccount, name='viewAccount'),
    path('chartOfAccounts/edit/', views.edit_account, name='edit_account'),
    path('chartOfAccounts/update/', views.update_account, name='update_account'),
    path('chartOfAccounts/add', views.add_account, name='add_account'),
    path('chartOfAccounts/delete',
         views.delete_account, name='delete_account'),
    path('chartOfAccounts/viewEventLog/', views.eventlog, name='EventLog'),
    path('listOfJournals/', views.listJournals, name='listOfJournals'),
    path('addJournal/', views.addJounral, name='addJournal'),
    # Django Admin Forgot Password Functionalities
    path('forgotPass/', auth_views.PasswordResetView.as_view(
        template_name='forgotPass.html'), name="reset_password"),
    path('emailSent/', auth_views.PasswordResetDoneView.as_view(
        template_name='emailSent.html'), name="password_reset_done"),
    path('passwordReset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='passwordReset.html'), name="password_reset_confirm"),
    path('passwordConfirm/', auth_views.PasswordResetCompleteView.as_view(
        template_name='passwordConfirm.html'), name="password_reset_complete"),
]
