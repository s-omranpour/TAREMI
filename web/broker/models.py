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
    number = models.IntegerField()

    def __str__(self):
        return self.question

    class Meta:
        constraints = [models.UniqueConstraint(fields=['form', 'number'], name='unique_form_number')]


class ApplicationResponse(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField("date_submitted", auto_now=True)

    class Meta:
        # constraints = 

    def get_form(self):
        return self.answers.first().form


class Answer(models.Model):
    class Meta:
        question_class = None

    response = models.ForeignKey(StudentResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(_meta.question_class, on_delete=models.CASCADE)

class TextualQuestion(Question):
    pass
class TextAnswer(Answer):
    class Meta:
        question_class = TextualQuestion

    value = models.CharField('text_value', max_length=100)
    def __str__(self):
        return self.value

class MultiChoiceQuestion(Question):
    pass
class MultiChoiceAnswer(Answer):
    class Meta:
        question_class = MultiChoiceQuestion
    value = models.CharField("choice_value", max_length=CHOICE_MAX_LENGTH)

    def __str__(self):
        return self.value


class NumericalQuestion(Question):
    pass
class NumericalAnswer(Answer):
    class Meta:
        question_class = NumericalQuestion
    value = models.IntegerField('int_value')

    def __str__(self):
        return self.value
