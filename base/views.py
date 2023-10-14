from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request,'home.html')

def maths(request):
    return render(request,'maths.html')

def science(request):
    return render(request,'science.html')

def english(request):
    return render(request,'english.html')
