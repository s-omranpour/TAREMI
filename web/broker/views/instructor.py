from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import *
from ..forms import render_form

@login_required(login_url='/account/login')
def instructor_home(request):
    user = request.user
    forms = user.instructor.forms.all()
    return render(request, 'broker/instructor/home.html', context={'user':user, 'forms':forms })


@login_required(login_url='/account/login')
def instructor_form_detail(request, id):
    user = request.user
    form = ApplicationForm.objects.filter(id=id).first()
    # if isinstance(form, EmptyQuerySet):
    #     # todo: error
    #     pass
    #responses = [answer.response for answer in form.questions.first().answers.all()]
    responses = ApplicationResponse.objects.filter(answers__question__form = form).distinct()
    return render(request, 'broker/instructor/form.html', context={'form':form , 'responses':responses})


@login_required(login_url='/account/login')
def instructor_response_detail(request, id):
    user = request.user
    response = ApplicationResponse.objects.filter(id=id).first()
    form = response.get_form()
    html = render_form(form, response, False)

    # if isinstance(response, EmptyQuerySet):
    #     # todo: error
    #     pass
    return render(request, 'broker/instructor/response.html', context={'html':html})


@login_required(login_url='/account/login')
def instructor_create_form(request):
    return
