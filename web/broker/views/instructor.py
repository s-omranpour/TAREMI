from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from ..models import *

@login_required()
def instructor_home(request):
    user = request.user
    forms = user.instructor.forms.all()
    return render(request, 'broker/instructor/home.html', context={'user':user, 'forms':forms })


@login_required()
def instructor_form_detail(request, id):
    user = request.user
    form = ApplicationForm.objects.filter(id=id).first()
    if isinstance(form, EmptyQuerySet):
        # todo: error
        pass
    responses = [answer.response for answer in form.questions.first().answers.all()]
    constext = {'form':form , 'responses':responses}
    return HttpResponse(form.info)


@login_required()
def instructor_response_detail(request, id):
    user = request.user
    response = ApplicationResponse.objects.filter(id=id).first()
    if isinstance(response, EmptyQuerySet):
        # todo: error
        pass
    return HttpResponse(response)

# TODO move this shit to API
@csrf_exempt
@login_required()
def instructor_create_form(request):
    if request.method == "GET":
        return render(request, 'broker/instructor/form_creation.html', {})
    else:
        form = ApplicationForm(creator=request.user.instructor)
        form.deadline = form.release_date + timedelta(days=10)
        form.course_id = request.POST["course"]
        form.info = request.POST["info"]
        form.save()
        for i in range(1, int(reqest.POST["length"]) + 1):
            if request.POST["q_%d_type" % i] == "textual":
                q = TextualQuestion(form=form, question=request.POST["q_%d_body" % i], number=i)
                q.save()

        return HttpResponse();
