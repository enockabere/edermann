from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'main/landing.html')
def estate(request):
    return render(request,'main/estate.html')
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