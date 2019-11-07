from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'broker/home.html', context={})

def display(request):
    return HttpResponse('See Asghar : %s' % display_form(ApplicationResponse.objects.first()))

def display_form(res: ApplicationResponse):
    html = ""
    for a in res.answers.order_by('question__number'):
        html += "<p> {} </p>".format(str(a.question)) + "<p>{}</p>".format(str(a))
    return html

        