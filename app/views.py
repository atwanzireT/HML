from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    services = Service.objects.all()[:3]
    rooms = Room.objects.all()[:3]

    dic = {
        'services': services,
        'rooms': rooms,
    }
    return render(request, 'index.html', dic)

def contact(request):
    return render(request, 'contact.html')

def rooms(request):
    rooms = Room.objects.all()
    room_image = Room_Image.objects.all()

    dic = {
        'rooms': rooms,
        'room_image': room_image,
    }
    return render(request, 'rooms.html', dic)

def blog(request):
    blog = Update.objects.all()
    category = Update_Category.objects.all().order_by('?')[:6]
    blog_slice = Update.objects.all()[:4]
    dic = {
        'blog':blog,
        'blog_slice':blog_slice,
        'category' : category,
    }
    return render(request, 'blog.html', dic)
