from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'main/landing.html')
def sketch(request):
    return render(request,'main/sketch.html')
def block(request):
    return render(request,'main/block.html')
def floor(request):
    return render(request,'main/floor.html')