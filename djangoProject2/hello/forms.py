from .models import Autorization,Reaction
from django.forms import ModelForm,TextInput,Select,Textarea
from django import forms

# from .src.data_for_us import get_date_for_user
import datetime
class AuthorizationForm(ModelForm):
    class Meta:
        model=Autorization
        fields=['login','password']
        widgets={"login":TextInput(attrs={
            "type":"text",
            "name":"login",
            "placeholder":"Введите фамилию",
        }),

            "password": TextInput(attrs={
                "type": "password",
                "name": "password",
                "placeholder": "Введите пароль",
            })}
# class ReactionForm(ModelForm):
#     class Meta:
#         model=Reaction
#         fields=['like']
#         widgets={"login":Butt(attrs={
#
#         })}