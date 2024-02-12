# views.py

from django.shortcuts import render



def kontak(request):
    context = {
        "name": "Halaman Kontak",
    }
    return render(request, "kontak.html", context)
