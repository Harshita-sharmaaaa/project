from django.shortcuts import render,redirect
from education.models import *
from education.forms import *
from django.contrib.auth import login, authenticate 
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'website.html')
def about(request):
    return render(request,'about.html')
def courses(request):
    return render(request,'courses.html')
def camp(request):
    return render(request,'campus life.html')
def extra(request):
    return render(request,'extra.html')
def accesbility(request):
    return render(request,'accesbility.html')
def information(request):
    return render(request,'information.html')

# Create your views here.
def apply(request):
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html')

def subs(request):
    if request.method=="POST":
        form=subs1(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'about.html')

def apply(request):
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html')

def apply1(request):
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"website.html")

def apply2(request):
    if request.method=="POST":
        form=subscribe1(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'website.html')
def log(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home/')
    else:
        form=loginform()
    return render(request,'registration/signup.html',{'form':form})
