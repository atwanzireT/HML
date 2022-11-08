from django.contrib import admin
from .models import *

# Register your models here.
class RoomImageInline(admin.TabularInline):
    model = Room_Image
    extra = 5

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

class RoomImageInline(admin.TabularInline):
    model = Service_Image
    extra = 5

class ServiceAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

admin.site.register(Room, RoomAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking)
admin.site.register(Update)
admin.site.register(Update_Category)