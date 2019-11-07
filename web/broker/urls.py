from django.urls import path
from . import views


urlpatterns = [
    path('', views.instructor_home, name='display'),
    path('', views.form_filling, name='display'),
]