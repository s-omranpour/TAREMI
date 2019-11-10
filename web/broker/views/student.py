from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import render

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
    resp = ApplicationResponse()
    for q in form.questions.all():
        t = q.typed().make_answer()
        t.response = resp

    resp.answers.all()
    return render(request, 'broker/student/application.html', context={'form': render(form)})
