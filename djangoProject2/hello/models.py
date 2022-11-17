from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
class Autorization(models.Model):
    login = models.CharField('Логин', max_length=20)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.login
class Film(models.Model):
    title=models.CharField('Название фильма',max_length=20)
    def __str__(self):
        return self.title
class Reaction(models.Model):
    login = models.ForeignKey(Autorization, on_delete=models.CASCADE)
    like=models.CharField('Реакция',max_length=20)
    film=models.ForeignKey(Film,on_delete=models.CASCADE)
