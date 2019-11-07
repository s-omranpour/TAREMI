from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Student


def login_user(request):
    # TODO get redir from POST/GET
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


def signup_user(request):
    # TODO get redir from POST/GET
    redirect_to = settings.LOGIN_REDIRECT_URL

    if request.user.is_authenticated:
        return redirect(redirect_to)

    if request.method == 'POST':
        # TODO make user is_active=False, then send activation email
        user = User(username='s_' + request.POST['student_id'])
        user.set_password(request.POST['password'])
        user.save()
        student = Student(user=user, student_id=request.POST['student_id'])
        student.save()

        login(request, user)
        return render(request, 'authentication/signup/verification.html', \
            {'message' : 'Your account was successfully created.', 'type' : 'success'})

    return render(request,'authentication/signup/signup.html',{})
