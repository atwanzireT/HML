from django.db import models
import uuid
from app.models import *

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.EmailField()
    status = models.CharField(max_length=50)
    slug = models.SlugField()


    def __str__(self):
        return f"{self.first_name} {self.last_names}"

class Booking(models.Model):
    booking_id = models.UUIDField(default = uuid.uuid4, unique = True)
    email = models.EmailField(blank=True, null=True)
    check_InDate = models.DateField()
    check_OutDate = models.DateField()
    no_of_Guests = models.IntegerField(default = 1)
    room_booked = models.ForeignKey(Room, on_delete = models.CASCADE)
    slug = models.SlugField(blank = True, null = True)