from django.shortcuts import redirect, render
from django.views import View
from django_daraja.mpesa.core import MpesaClient
from django.contrib import messages
import requests
import json

# Create your views here.
cl = MpesaClient()
stk_push_callback_url = 'https://darajambili.herokuapp.com/express-payment'


class Payments(View):
    def get(self, request):
        
        return render(request, 'main/payment.html')

    def post(self, request):
        try:
            if request.method == 'POST':
                token = cl.access_token()
                print(token)
                phone_number = request.POST.get('phone_number')
                amount = int(request.POST.get('amount'))
                account_reference = request.POST.get('account_reference')
                transaction_desc = 'Description'

                callback_url = stk_push_callback_url
                r = cl.stk_push(
                    phone_number, amount, account_reference, transaction_desc, callback_url)
                messages.success(request, r.response_description)
                print(r.json())
                return redirect('pay')
        except Exception as e:
            print(e)
            return redirect('pay')
