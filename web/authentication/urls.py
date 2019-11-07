from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    # path('reset', views.reset_password, name='reset_psswd')
]