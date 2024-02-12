# views.py

from django.shortcuts import render

def index(request):
    context = {
        'name': 'Hello Woy',  
    }
    return render(request, 'index.html', context)