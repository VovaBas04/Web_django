from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns = [
    path('',views.registr),
    path('signin',views.signin),
    path('registration',views.registratrion,name='registration'),
    path('signup',views.signup),
    path('exit',views.registr),
    path('join/<int:id>/<int:number>',views.send_reaction)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)