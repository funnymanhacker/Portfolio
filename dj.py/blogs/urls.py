from django.urls import path,include
from .views import *
from.views import authview

urlpatterns = [
    path('index/',index,name="index"),
    path('old/',old,name="old"),
    path('new/',abi,name="abi"),
    path('home/',Home,name='home'),
    path('account/',include("django.contrib.auth.urls")),
    path('registration/signup/',authview,name='signup'),
    path('about/',about),
   
]