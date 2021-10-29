from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path('sketch',views.sketch,name="sketch"),
    path('block',views.block,name="block"),
    path('floor',views.floor,name="floor"),
]