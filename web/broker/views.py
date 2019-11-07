
from django.shortcuts import render, redirect
from django.db.models.query import EmptyQuerySet

from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    user = request.user
    try:
        if user.student:
            return redirect('student_home')
    except:
        return redirect('instructor_home')


def student_home(student):
    pass

@login_required(login_url='/account/login')
def instructor_home(request):
    user = request.user
    forms = user.instructor.forms.all()
    responses = [len([answer.response for answer in form.questions.first().answers.all()]) for form in forms]
    return render(request, 'broker/instructor_home.html', context={'user':user, 'form_res':zip(forms,responses)})


@login_required(login_url='/account/login')
def instructor_form_detail(request, id):
    user = request.user
    form = ApplicationForm.objects.filter(id=id).first()
    if isinstance(form, EmptyQuerySet):
        # todo: error
        pass
    responses = [answer.response for answer in form.questions.first().answers.all()]
    constext = {'form':form , 'responses':responses}
    return HttpResponse(form.info)


@login_required(login_url='/account/login')
def instructor_response_detail(request, id):
    user = request.user
    response = ApplicationResponse.objects.filter(id=id).first()
    if isinstance(response, EmptyQuerySet):
        # todo: error
        pass
    return HttpResponse(response)


@login_required(login_url='/account/login')
def instructor_create_form(request):
    return 

def form_filling(request):
    return render(request, 'broker')

def display(request):
    return HttpResponse('See Asghar : %s' % display_form(ApplicationResponse.objects.first()))


def display_form(res: ApplicationResponse):
    html = ""
    for a in res.answers.order_by('question__number'):
        html += "<p> {} </p>".format(str(a.question)) + "<p>{}</p>".format(str((TextAnswer)(a)))
    return html
