from django.urls import path
from . import views


urlpatterns = [
    path('', views.broker_form, name='index'),
]