from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile),
    path('test/', views.test),
    path('login/', views.login),
    path('newUser/', views.newUser),
]
