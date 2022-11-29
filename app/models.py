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
    description = RichTextField(blank = True, null = True)
    halfboard_price = models.FloatField(default=0)
    fullboard_price = models.FloatField(default=0)
    slug = models.SlugField(blank=True, null=True)

    def price(self):
        average_price = self.halfboard_price + self.fullboard_price
        average_price = (average_price / 4)
        return average_price


    def __str__(self):
        return self.title


class Update_Category(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    description = RichTextField(blank = True, null = True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self) -> str:
        return self.title

class Update(models.Model):
    category = models.ForeignKey(Update_Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'updates')
    description = RichTextField(blank = True)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Room_Image(models.Model):
    title = models.CharField(max_length = 50)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    image = models.ImageField(blank = True, null = True)

    def __str__(self):
        return self.title

class Service_Image(models.Model):
    title = models.CharField(max_length = 50)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    image = models.ImageField(blank = True, null = True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name

