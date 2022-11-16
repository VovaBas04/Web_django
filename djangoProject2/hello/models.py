from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
class Autorization(models.Model):
    login = models.CharField('Логин', max_length=20)
    password = models.CharField('Пароль', max_length=20)
class Reaction(models.Model):
    login = models.CharField('Логин', max_length=20)
    like=models.CharField('Реакция',max_length=20)