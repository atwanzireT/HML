from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from management.forms import *

# Create your views here.
def index(request):
    form = BookingForm(request.POST)
    if request.method == 'POST': # check post
        if form.is_valid():
            form.save()  #save data to table
            return HttpResponseRedirect('/')
    form = BookingForm
    services = Service.objects.all()[:3]
    rooms = Room.objects.all()[:3]

    dic = {
        'form':form,
        'services': services,
        'rooms': rooms,
    }
    return render(request, 'index.html', dic)

def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST': # check post
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            return HttpResponseRedirect('/contact/')
    form = ContactForm
    dic = {
        'form':form,
    }
    return render(request, 'contact.html', dic)

def service(request):
    service = Service.objects.all()
    paginator = Paginator(service, 9)
    page = request.GET.get('page')
    service = paginator.get_page(page)

    dic = {
        'service': service,
    }
    return render(request, 'services.html', dic)

def rooms(request):
    rooms = Room.objects.all()
    room_image = Room_Image.objects.all()
    paginator = Paginator(rooms, 9)
    page = request.GET.get('page')
    rooms = paginator.get_page(page)

    dic = {
        'rooms': rooms,
        'room_image': room_image,
    }
    return render(request, 'rooms.html', dic)

def blog(request):
    blog = Update.objects.all()
    category = Update_Category.objects.all().order_by('?')[:6]
    blog_slice = Update.objects.all()[:4]
    blog_rand = Update.objects.all().order_by('?')[:3]
    dic = {
        'blog':blog,
        'blog_slice':blog_slice,
        'category' : category,
        'blog_rand':blog_rand,
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