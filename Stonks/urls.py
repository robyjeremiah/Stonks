from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Login Views
    path('', views.index, name='index'),
    path('generalHome/', views.generalHome, name='userHome'),
    path('logout/', views.loggedOut, name='loggedOut'),
    # Create User Views
    path('newUser/', views.newUser, name='newUser'),
    # Forgot Password View
    path('security/', views.security, name='security'),
    path('passwordConfirm/', views.passwordConfirm, name='passwordConfirm'),
    # Administrator Home
    path('adminHome/', views.adminHome, name='adminHome'),
    path('adminHome/delete/<pk>', views.delete_user, name='delete_user'),
    path('adminHome/edit/ajax/user', views.getUserInfo, name='getUserInfo'),
    path('chartOfAccounts/', views.chartOfAccounts, name='chartOfAccounts'),
    # Django Admin Forgot Password Functionalities
    path ('forgotPass/', auth_views.PasswordResetView.as_view(template_name='forgotPass.html'), name="reset_password"),
    path ('emailSent/', auth_views.PasswordResetDoneView.as_view(template_name='emailSent.html'), name="password_reset_done"),
    path ('passwordReset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='passwordReset.html'), name="password_reset_confirm"),
    # path ('passwordConfirm/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordConfirm.html'), name="password_reset_complete"),
    path('viewAccountInfo/', views.useraccount, name='viewAccount')
]
