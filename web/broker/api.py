from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


from .models import *

@login_required(login_url='/account/login')
@csrf_exempt
def change_response_state(request):
    if request.method == 'POST':
        id = request.POST['id']
        state = request.POST['state']
        ApplicationResponse.objects.filter(id=id).update(state = state)
    return HttpResponse()