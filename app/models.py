from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = "services")
    description = RichTextField(blank = True)

    def __str__(self):
        return self.title

class Room(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'rooms')
    description = RichTextField(blank = True)
    price = models.FloatField()

    def __str__(self):
        return self.description

class Booking(models.Model):
    booking_id = models.UUIDField(default = uuid.uuid4, unique = True)
    booking_in = models.DateField()
    booking_out = models.DateField()
    room_booked = models.ForeignKey(Room, on_deleted = models.CASCADE)

    def __str__(self):
        return self.booking_id

class Update(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'updates')
    description = RichTextField(blank = True)

    def __str__(self) -> str:
        return self.title