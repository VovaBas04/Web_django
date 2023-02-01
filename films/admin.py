from django.contrib import admin
from .models import *

# Register your models here.
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id','username','like','title']
    list_editable= ['username','like','title']
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id','title','overflew','director']
    list_editable= ['title','overflew','director']
admin.site.register(Reaction,ReactionAdmin)
admin.site.register(Film,FilmAdmin)