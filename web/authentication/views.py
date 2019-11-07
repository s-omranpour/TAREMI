from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings


def login_user(request):
    redirect_to = settings.LOGIN_REDIRECT_URL

    if request.user.is_authenticated:
        return redirect(redirect_to)

    if request.method == 'POST':
        req = request.POST
        user = authenticate(username=req['username'], password=req['password'])
        if not user:
            return render(request,'authentication/login.html',{'error_message': 'Wrong password'})
        else:
            login(request, user)
            return redirect(redirect_to)

    return render(request,'authentication/login.html',{})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

# def reset_password(request):
    # if request.method == 'POST':
    #     req = request.POST
    #     email = req['email']
    #     user = User.objects.filter(email=email)
    #     if user:
            
    #     return HttpResponse('DONE!')

    # return render(request,'authentication/reset_password.html',{})