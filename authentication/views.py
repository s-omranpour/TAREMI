from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def login(request):
    return render(request,'authentication/login.html',{})
