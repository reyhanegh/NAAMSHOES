from django.urls import path
from RGHwebsite.views import *

urlpatterns = [
    path('about/', about, name = 'about'),
    path('contact/', contact, name='contact'),
    path('', home, name='index')


]