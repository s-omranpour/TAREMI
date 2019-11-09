from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import *

@login_required(login_url='/account/login')
def instructor_home(request):
    user = request.user
    forms = user.instructor.forms.all()
    return render(request, 'broker/instructor/home.html', context={'user':user, 'forms':forms })


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
