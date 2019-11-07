from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)
    major = models.CharField(max_length=50)
    enterance_year = models.CharField(max_length=4)


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)


