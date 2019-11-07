from django.shortcuts import render

# Create your views here.


def broker_form(request):

    return render(request, 'broker/instructor_home.html', context={})
