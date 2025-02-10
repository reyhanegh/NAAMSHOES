from django.urls import path
from RGHwebsite.views import *


urlpatterns = [
    path('about/', about_view, name = 'about'),
    path('contact/', contact_view, name='contact'),
    path('', home_view, name='index')


]