from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:id>', views.blog_detail, name='blog_detail'),

]