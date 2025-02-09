from django.urls import path
from RGHwebsite.views import *

urlpatterns = [
    path('aboutUs/', aboutUs),
    path('', home)


]