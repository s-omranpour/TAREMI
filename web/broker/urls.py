from django.urls import path,re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student_home, name='student_home'),
    path('instructor', views.instructor_home, name='instructor_home'),
    re_path('instructor/forms/<int:id>/', views.instructor_form_detail, name='form_detail'),
    re_path('instructor/res/<int:id>/', views.instructor_response_detail, name='res_detail'),
]