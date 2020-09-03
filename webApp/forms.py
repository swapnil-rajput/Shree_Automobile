from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.messages import error
from django.forms import ModelForm
from django.contrib.auth.models import User
from webApp.models import customer, vehicle
import re


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    name = forms.CharField(label='Name',
     widget=forms.TextInput(attrs={
         'class': 'form-control',
         'placeholder': 'Enter your name'}))
    last_name = forms.CharField(label='Last name',
     widget=forms.TextInput(attrs={
         'class': 'form-control',
         'placeholder': 'Enter your last name'}))
    username = forms.CharField(label='Username',
     widget=forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your user Id'}))

    email = forms.EmailField(label='Email',
     widget=forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter your email'}))
    password = forms.CharField(label='Password',
     widget=forms.PasswordInput(attrs={
         ' class': 'form-control',
          'placeholder': 'Enter your password'}))
    password1 = forms.CharField(label='Confirm password',
     widget=forms.PasswordInput(attrs={
          'class': 'form-control',
          'placeholder': 'Enter password again'}))
    address = forms.CharField(label='Address', required=False,
     widget=forms.Textarea(attrs={
         'class': 'form-control',
         'placeholder': 'Enter your address',
         'rows': '5',
         'cols': '10'}))
    mobile_no = forms.IntegerField(label='Mobile No.',
     widget=forms.TextInput(attrs={
         'class': 'form-control',
         'placeholder': 'Enter your mobile number'}))

    def clean_username(self):
        uname = self.cleaned_data['username']
        if customer.objects.filter(username=uname).exists():
            raise forms.ValidationError(("*Username already exists"),code='invalid')

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        rvalpass = self.cleaned_data['password1']

        if valpass != rvalpass:
            raise forms.ValidationError(("*Password does not match"), code='invalid')

    class Meta:
        model = customer
        fields = '__all__'


v_type = [('Car', 'Car'), ('SUV', 'SUV')]


class VehicleForm(forms.ModelForm):
    username = forms.CharField(label='Username', error_messages={'required': 'enter your username'},
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter your user Id'
                               }))

    type = forms.CharField(label='Type', widget=forms.Select(choices=v_type))
    number = forms.CharField(label='Number',
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Enter vehicle number'
                             }))

    def clean(self):
        cleaned_data = super().clean()
        uname = self.cleaned_data['username']
        num = self.cleaned_data['number']
        if customer.objects.filter(username=uname):
            pass
        else:
            raise forms.ValidationError("Username does not exits")
        if re.search("[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4}", num):
            pass
        else:
            raise forms.ValidationError("Enter correct vehicle number")

    owner = forms.CharField(label='Owner Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter owner name'
    }))

    class Meta:
        model = vehicle
        fields = '__all__'

