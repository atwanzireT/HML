from django.db import models
import uuid
from app.models import *

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_names}"

class Booking(models.Model):
    booking_id = models.UUIDField(default = uuid.uuid4, unique = True)
    booking_in = models.DateField()
    booking_out = models.DateField()
    room_booked = models.ForeignKey(Room, on_delete = models.CASCADE)

    def __str__(self):
        return self.booking_id