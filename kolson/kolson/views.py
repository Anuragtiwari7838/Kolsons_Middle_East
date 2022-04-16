from django.shortcuts import render
from kolsons.models import Product, clientsM

def index(request):
    client = clientsM.objects.all()
    return render(request, 'index.html',{'client':client})

def products(request):
    return render(request,'kolsons/enquiry.html')