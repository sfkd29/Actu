from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models

# Create your views

def index(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request,'pages/index.html',data) 



def fap(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return JsonResponse(data,safe=False)