from django.db import models
from django.contrib.auth.models import User
import authentication.constants as CONSTANTS
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=False, default=999999)
    major = models.CharField(max_length=2, choices=CONSTANTS.MAJORS, default='1')
    enterance_year = models.IntegerField(null=False, default=1395)

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)