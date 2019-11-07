from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student_home, name='student_home'),
    path('instructor', views.instructor_home, name='instructor_home')
]