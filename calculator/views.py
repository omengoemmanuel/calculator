from django.shortcuts import render, HttpResponse
from django.urls import path


# Create your views here.

def cal(request):
    return HttpResponse('welcome home')
