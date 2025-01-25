from django.shortcuts import render
import razorpay
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Registration 
# Create your views here.


def home(request):
    return render (request,"home.html")


def demo(request):
    return render (request ,"demo.html")


def about(request):    
    return render (request,"about.html")

def registeration(request):
    return render (request,"registration.html")