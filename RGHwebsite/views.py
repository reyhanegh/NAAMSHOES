from django.shortcuts import render
from django.http import HttpResponse

def aboutUs(request):
    return render(request, 'aboutUs.html')

def home(request):
    return HttpResponse('<h1> Welcome to ReyahenGhafouripour  Programming Academy </h1>')