from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile),
    path('test/', views.test),
    path('login/', views.login),
    path('newUser/', views.newUser),
    path('forgotPass/', views.forgotPass),
    path('security/', views.security),
    path('emailSent/', views.emailSent),
    path('passwordReset/', views.passwordReset),
    path('passwordConfirm/', views.passwordConfirm),
]
