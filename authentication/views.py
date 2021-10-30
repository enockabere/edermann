from django.shortcuts import render

# Create your views here.
def login_request(request):
    return render(request,'accounts/auth.html')
# def account_request(request):
#     return render(request,'accounts/account.html')