from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class addCarForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['nombre','patente','color','ndepuertas', 'imagen', 'precio']
    
                                                              
                               