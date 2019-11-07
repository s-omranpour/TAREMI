
from django.shortcuts import render, redirect

from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    user = request.user
    if user.student:
        return redirect('student_home')
    return

def instructor_home(instructor):
    pass


def student_home(student):
    pass

@login_required(login_url='/account/login')
def instructor_home(request):
    return render(request, 'broker/instructor_home.html', context={})

def form_filling(request):
    return render(request, 'broker')

def display(request):
    return HttpResponse('See Asghar : %s' % display_form(ApplicationResponse.objects.first()))


def display_form(res: ApplicationResponse):
    html = ""
    for a in res.answers.order_by('question__number'):
        html += "<p> {} </p>".format(str(a.question)) + "<p>{}</p>".format(str((TextAnswer)(a)))
    return html
