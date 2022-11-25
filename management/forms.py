from django.forms import ModelForm, TextInput, Select
from .models import *
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'status']


class BookingForm(ModelForm):
    check_InDate = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }))
    check_OutDate = forms.DateField(widget=forms.DateInput(format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'type':'email'
        }), required=True)
    class Meta:
        model = Booking
        fields = ['email', 'check_InDate', 'check_OutDate', 'no_of_Guests', 'room_booked']
        widgets = {
            'email':TextInput(attrs={'class': 'form-control',}),
            'no_of_Guests': TextInput(attrs={'class': 'form-control',}),
            'room_booked': Select(attrs={'class': 'form-select'}),
        }
        