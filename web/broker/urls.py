from django.urls import path,re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student_home, name='student_home'),
    path('apply/<int:id>/', views.application, name='apply_form'),
    path('apply/success/', views.application_success, name='application_success'),
    path('instructor/', views.instructor_home, name='instructor_home'),
    path('instructor/form/new/', views.instructor_create_form, name='create_form'),
    path('instructor/form/<int:id>/', views.instructor_form_detail, name='form_detail'),
    path('instructor/res/<int:id>/', views.instructor_response_detail, name='res_detail'),
]
