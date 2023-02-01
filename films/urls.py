from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('about/',about,name='about'),
    path('login/',LoginUser.as_view(),name='login'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('logout/',logout_user,name='logout'),
    path('recom/',recom,name='recom'),
    path('join/<int:id_film>/<int:number>',send_reaction),
    path('lkuser/',kabinet,name='kabinet'),
    path('lkuser/<int:number>',kabinet_control,name='kabinet_control'),
    path('lkuser/password-change/', ChangePasswordView.as_view(), name='password_change')
]
