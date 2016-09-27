from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def fun1(request):

    return HttpResponse("hello world by fun1")

def fun2(request):

    return HttpResponse("hello world by fun2")

def fun3(request):

    return HttpResponse("hello world by fun3")