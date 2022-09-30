from django.urls import path
from . import views

urlpatterns = [
    path('pay', views.Payments.as_view(), name='pay'),
]
