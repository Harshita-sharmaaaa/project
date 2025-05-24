from django import forms
from education.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

class subs1(forms.ModelForm):
    class Meta:
        model=subsc
        fields='__all__'


class subscribe1(forms.ModelForm):
    class Meta:
        model=subscribe
        fields='__all__'

class loginform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2',)