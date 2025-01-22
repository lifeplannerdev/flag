from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request,"home.html")


def demo(request):
    return render (request ,"demo.html")


def about(request):    
    return render (request,"about.html")


def registeration(request):
    return render (request,"registration.html")    