from django.urls import path
from RGHwebsite.views import *

urlpatterns = [
    path('about/', about),
    path('contact/', contact),
    path('', home)


]