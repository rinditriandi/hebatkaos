from django.shortcuts import render

from .models import General

def index(request):
    qs = General.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'base.html', context)

def contact(request):
    return render(request, 'profile/contact_us.html', {})

def about(request):
    return render(request, 'profile/about.html', {})

