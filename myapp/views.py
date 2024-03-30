from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return HttpResponse("Salom")

def about_page(request):
    return HttpResponse("Xayr")

def visit_page(request):
    return HttpResponse("saytimizga xush kelibsiz")

def center_page(request):
    return HttpResponse("bu yer bizning ceterimiz")