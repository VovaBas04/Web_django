from django.urls import path
from . import views
urlpatterns = [
    path('',views.registr),
    path('signin',views.signin),
    path('registration',views.registratrion,name='registration'),
    path('signup',views.signup),
    path('exit',views.registr),
    path('join/<int:id>/<int:number>',views.send_reaction)
]