from authentication.models import *
from django.contrib.auth.models import User

def make_student(first_name, last_name, uname, password, major, stdid):
    u = User(username=uname, first_name=first_name, last_name=last_name)
    u.set_password(password)
    u.save()
    student = Student(user=u, student_id=stdid, major=major)
    student.save()
    return student

def make_instructor(first_name, last_name, uname, password):
    u = User(username=uname, first_name=first_name, last_name=last_name)
    u.set_password(password)
    u.save()
    instructor = Instructor(user=u)
    instructor.save()
    return instructor

st1 = make_student('ali', 'alavi', 'ali', '1234', 'ce', 105721)
st2 = make_student('ghasem', 'ghasemi', 'ghasem', '1234', 'ce', 105789)
in1 = make_instructor('javad', 'javadi', 'javad', '1234')
in2 = make_instructor('mamad', 'mamadi', 'mamad', '1234')
in3 = make_instructor('reza', 'rezayi', 'reza', '1234')