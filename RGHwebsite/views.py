from django.shortcuts import render
from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse('<h1> I am AI developer </h1>')

def home(request):
    return HttpResponse('<h1> Welcome to ReyahenGhafouripour  Programming Academy </h1>')