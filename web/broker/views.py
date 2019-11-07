from django.shortcuts import render, redirect
from .models import *

def home(request):
    user = request.user
    if user.student:
        return redirect('student_home')
    return

def instructor_home(instructor):
    pass


def student_home(student):
    pass

def display(request):
    return HttpResponse('See Asghar : %s' % display_form(ApplicationResponse.objects.first()))

def display_form(res: ApplicationResponse):
    html = ""
    for a in res.answers.order_by('question__number'):
        html += "<p> {} </p>".format(str(a.question)) + "<p>{}</p>".format(str(a))
    return html

        