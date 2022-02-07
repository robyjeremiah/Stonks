from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/', views.newUser, name='newUser'),
    path('forgotPass/', views.forgotPass, name='forgotPass'),
    path('security/', views.security, name='security'),
    path('emailSent/', views.emailSent, name='emailSent'),
    path('passwordReset/', views.passwordReset, name='passwordReset'),
    path('passwordConfirm/', views.passwordConfirm, name='passwordConfirm'),
    path('generalHome/', views.generalHome, name='userHome'),
    path('adminHome/', views.adminHome, name='adminHome'),
]
