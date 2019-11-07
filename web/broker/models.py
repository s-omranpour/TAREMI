from django.db import models

from broker.constants import *
from authentication.models import Instructor, Student


class ApplicationForm(models.Model):
    course_id = models.CharField("course_id", max_length=10)
    creator = models.ForeingKey(Instructor, on_delete=models.CASCADE)
    release_date = models.DateField("release_date", auto_now=True)
    deadline = models.DateField("deadline", auto_now=True)
    info = models.CharField("information", max_length=1000)

class Question(models.Model):
    form = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("question", max_length=QUESTION_MAX_LENGTH)


class ApplicationResponse(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField("date_submitted", auto_now=True)

class Answer(models.Model):
    class Meta:
        question_class = None

    response = models.ForeignKey(StudentResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(_meta.question_class, on_delete=models.CASCADE)

class TextualQuestion(Question):
    pass
class TextAnswer(Answer):
    value = models.CharField('text_value', max_length=100)

class MultiChoiceQuestion(Question):
    pass
class MultiChoiceAnswer(Answer):
    value = models.CharField("choice_value", max_length=CHOICE_MAX_LENGTH)


class NumericalQuestion(Question):
    pass
class NumericalAnswer(Answer):
    value = models.IntegerField('int_value')
