from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=False)

    class Meta:
        model=User
        #define the order of the fields
        fields=["username","email","password1","password2"] #except for email all fields are inbuililt ones
