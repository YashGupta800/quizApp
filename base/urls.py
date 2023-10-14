from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),  
    path('maths',views.maths, name="maths"), 
    path('science',views.science, name="science"),
    path('english',views.english, name="english"),
]
