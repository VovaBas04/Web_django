from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .forms import AuthorizationForm
from .models import Autorization,Reaction
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
            if logins.get(login)[1]==password:
                dict_for_error.update({'name': login})
                dict_for_error.update({'id':logins.get(login)[0]})
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
                dict_for_error.update({'id': logins.get(login)[0]})
                form.save()
                return render(request,'hello/regist.html',dict_for_error)
            else:
                dict_for_error['error']=True
        else:
            dict_for_error['error']=True
        return render(request, 'hello/registration.html',dict_for_error)
def send_reaction(request,id,number):
    login=Autorization.objects.all().get(id=id).login
    print(login)
    dict={'id':id,"name":login}
    if request.method=='POST':
            if number==1:
                p=Reaction.objects.create(login=login,like="Понравилось")
            elif number==2:
                p=Reaction.objects.create(login=login,like="Не понравилось")
            else:
                p=Reaction.objects.create(login=login,like="Не смотрел")
    return render(request,'hello/authorization.html',dict)