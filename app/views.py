from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Koti(request):
    return HttpResponse('Koti is a all rounder')
def rama(request):
    return HttpResponse("Rama is a god")