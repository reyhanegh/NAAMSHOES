from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    context = {'name': 'ایمان', 'lastname':'حمیدخواه'}
    return render(request, 'website/about.html', context )

def contact_view(request):
    return render(request, 'website/contact.html' )