from django.urls import path
from . import views


urlpatterns = [
    path('dis', views.display, name='display'),
    path('', views.broker_form, name='index'),
]