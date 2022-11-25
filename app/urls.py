from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms, name='rooms'),
    path('services/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:id>/', views.blog_detail, name='blog_detail'),
    path('rooms/<str:id>/', views.room_detail, name='room_detail'),
    path('services/<str:id>/', views.service, name = 'service'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]