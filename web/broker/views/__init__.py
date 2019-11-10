from django.shortcuts import redirect

from .student import *
from .instructor import *

def home(request):
    user = request.user
    try:
        if user.student:
            return redirect('student_home')
    except:
        return redirect('instructor_home')
