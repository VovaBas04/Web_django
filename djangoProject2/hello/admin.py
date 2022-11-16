from django.contrib import admin
from .models import Autorization,Reaction
from django.contrib.auth.models import User
# Register your models here.
class AutorizationAdmin(admin.ModelAdmin):
    list_display = ['id','login','password']
    list_editable= ['login','password']
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id','login','like']
    list_editable= ['login','like']
admin.site.register(Autorization,AutorizationAdmin)
admin.site.register(Reaction,ReactionAdmin)