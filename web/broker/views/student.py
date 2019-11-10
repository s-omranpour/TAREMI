from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template import Template
from ..forms import render_form, save_form

from ..models import *

@login_required()
def student_home(request):
    student = request.user.student
    forms = ApplicationForm.objects.exclude(questions__answers__response__owner=student)
    responses = student.responses.all()
    return render(request, 'broker/student/home.html', context={'user':request.user, 'forms':forms, 'responses': responses})

@login_required()
def application(request, id):
    form = ApplicationForm.objects.get(id=id)

    if request.method == "GET":
        form_template = Template(render_form(form, editable=True))
        form_html = form_template.render(RequestContext(request))
        return render(request, 'broker/student/application.html', context={'form': form_html})
    else:
        response = ApplicationResponse(owner=request.user.student, state = 'p')
        response.save()
        save_form(form, request.POST, response)

        return redirect('application_success')

def application_success(request):
    return render(request, 'broker/student/success.html', {'message' : 'Your Application Successfully Submited.'})
