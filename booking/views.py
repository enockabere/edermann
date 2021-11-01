from django.shortcuts import render
from . models import Estate,Apartment

# Create your views here.
def landing(request):
    estate = Estate.objects.all()
    ctx = {"estate":estate}
    return render(request,'main/landing.html',ctx)
def estate(request):
    apartment = Apartment.objects.all()
    ctx = {"apartment":apartment}
    return render(request,'main/estate.html',ctx)
def sketch(request):
    return render(request,'main/sketch.html')
def block(request):
    return render(request,'main/block.html')
def floor(request):
    return render(request,'main/floor.html')
def booking(request):
    return render(request,'main/booking.html')
def individual(request):
    return render(request,'main/individual.html')
def terms(request):
    return render(request,'main/terms.html')