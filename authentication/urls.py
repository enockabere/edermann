from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.login_request, name='login'),
    # path('acc', views.account_request,name="acc")
]