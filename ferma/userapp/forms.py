from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@gmail.com'}))
    first_name = forms.CharField(label='Імʼя', max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Прізвище', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    phone_number = forms.CharField(label='Номер телефону', max_length=15, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': '+380XXXXXXXXX'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'
