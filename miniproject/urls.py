
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('auth',imagelogin,name='imagelogin'),
    path('register_user',register,name='register'),
    path('logout',logout_user,name='logout'),
    path('login',login_user,name='login'),
    path('userprofile/<int:pk>',uprofile,name='uprofile'),
    path('forgotpassword',takeemail,name='takeemail'),
    path('opt',otp,name='otp'),
    path('profiles',profiles,name='profiles'),
    path('takeprofile',takeprofile,name='takeprofile'),
]