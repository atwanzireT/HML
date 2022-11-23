from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'email', 'status']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_id', 'booking_in', 'booking_out', 'room_booked']
        