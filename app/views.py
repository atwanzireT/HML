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
    return render(request, 'index.html')