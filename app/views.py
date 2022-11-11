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
    name = request.GET.get('name')
    print(name)
    return render(request, 'contact.html')

def service(request):
    service = Service.objects.all

    dic = {
        'service': service,
    }
    return render(request, 'services.html', dic)

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

def blog_detail(request, id):
    blog_obj = Update.objects.get(id = id)
    dic  = {
        'blog_obj':blog_obj,
    }
    return render(request, 'blog_details.html', dic)

def room_detail(request, id):
    room_obj = Room.objects.get(id = id)
    room_img = Room_Image.objects.filter(room = id)
    dic  = {
        'room_obj':room_obj,
        'room_img':room_img,
    }
    return render(request, 'room_details.html', dic)


def service_detail(request, id):
    service_obj = Service.objects.get(id = id)
    dic = {
        'service_obj':service_obj,
    }
    return render(request, 'service.html', dic)