from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .forms import AuthorizationForm
from .models import Autorization,Reaction,Film
from random import randint
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
import datetime
from django import forms
from django.db import models

def registr(request):
    return render(request,"hello/regist.html")
def get_all_users():
    users_form = Autorization.objects.all().values("login", "password","id")
    logins = {}
    for el in users_form:
        logins.update({el['login']: [el['id'],el['password']]})
    return logins
def signin(request):
    dict_for_error={'error':False}
    if request.method=='POST':
        form =AuthorizationForm(request.POST)
        if form.is_valid():
            login=form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            logins=get_all_users()
            print(logins)
            if logins.get(login)!=None and logins.get(login)[1]==password:
                arr_films = Film.objects.all()
                len_films = len(arr_films)
                f = arr_films[randint(0, len_films - 1)]
                dict_for_error.update({'name': login})
                dict_for_error.update({'id':logins.get(login)[0]})
                dict_for_error.update({'film':f.title})
                return render(request,'hello/authorization.html',dict_for_error)
            else:
                dict_for_error['error']=True
        else:
            dict_for_error['error']=True
        return render(request, 'hello/regist.html',dict_for_error)
def registratrion(request):
        return render(request,'hello/registration.html')
def signup(request):
    dict_for_error={'error':False}
    if request.method=='POST':
        form =AuthorizationForm(request.POST)
        if form.is_valid():
            login=form.cleaned_data.get("login")
            logins=get_all_users()
            print(logins)
            if logins.get(login)==None:
                dict_for_error.update({'name': login})
                form.save()
                return render(request,'hello/regist.html',dict_for_error)
            else:
                dict_for_error['error']=True
        else:
            dict_for_error['error']=True
        return render(request, 'hello/registration.html',dict_for_error)
def send_reaction(request,id,number):
    login=Autorization.objects.all().get(id=id)
    print(login)
    arr_films=Film.objects.all()
    len_films=len(arr_films)
    f=arr_films[randint(0,len_films-1)]
    dict={'id':id,"name":login.login,'film':f.title}
    if request.method=='POST':
            if number==1:
                p=Reaction.objects.create(login=login,like="Понравилось",film=f)
            elif number==2:
                p=Reaction.objects.create(login=login,like="Не понравилось",film=f)
            else:
                p=Reaction.objects.create(login=login,like="Не смотрел",film=f)
    return render(request,'hello/authorization.html',dict)