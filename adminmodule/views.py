from django.shortcuts import render

# Create your views here.

def adminview(request):
    
  return render (request,'dashboard.html')