from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    title = models.CharField('Название фильма',max_length=30)
    director = models.CharField('Режиссер',max_length=25)
    overflew = models.CharField('Описание',max_length=300,default=None)
    soup = models.CharField('РекСистем', max_length=200,default=None)

    def ovr(self):
        return self.overflew

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Reaction(models.Model):
    #username = models.CharField('Имя пользователя',max_length=20)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    like=models.CharField('Реакция',max_length=20)
    title=models.ForeignKey(Film,on_delete=models.CASCADE)
    recsys = models.IntegerField('Система рекомендаций',default=None)

    def likes(self):
        return self.like

    def __str__(self):
        return self.like

    class Meta:
        verbose_name = 'Реакция пользователя'
        verbose_name_plural = 'Реакции Пользователей'