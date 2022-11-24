from django.forms import ModelForm, TextInput
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'status']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['Check_InDate', 'Check_OutDate', 'No_of_Guests', 'room_booked']
        widgets = {
            'Check_InDate': TextInput(attrs={'class': 'form-control', 'id':'datepicker1',  'placeholder':'10/12/2020'}),
            'Check_OutDate': TextInput(attrs={'class': 'form-control', 'id':'datepicker1',  'placeholder':'10/12/2020'}),
            'No_of_Guests': TextInput(attrs={'class': 'form-control', 'id':'datepicker1'}),
            'room_booked': TextInput(attrs={'class': 'form-control'}),
        }
        