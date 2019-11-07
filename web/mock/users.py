from authentication.models import *
from django.contrib.auth.models import User


u = User(username='ali')
u.set_password('1234')
u.save()
student = Student(user=u, student_id=1234, major='ce')
student.save()

u2 = User(username='mamad')
u2.set_password('1234')
u2.save()
instructor = Instructor(user=u2)
instructor.save()