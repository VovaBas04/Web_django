from django.contrib import admin
from .models import Autorization,Reaction,Film
from django.contrib.auth.models import User
# Register your models here.
class AutorizationAdmin(admin.ModelAdmin):
    list_display = ['id','login','password']
    list_editable= ['login','password']
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id','login','like','film']
    list_editable= ['login','like','film']
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_editable= ['title']
admin.site.register(Autorization,AutorizationAdmin)
admin.site.register(Reaction,ReactionAdmin)
admin.site.register(Film,FilmAdmin)