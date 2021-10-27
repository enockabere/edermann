from django.shortcuts import render

# Create your views here.
def login_request(request):
    render(request,'accounts/auth.html')