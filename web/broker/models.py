from django.db import models

from broker.constants import *
from authentication.models import Instructor, Student


class ApplicationForm(models.Model):
    course_id = models.CharField("course_id", max_length=10)
    creator = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='forms')
    release_date = models.DateField("release_date", auto_now=True)
    deadline = models.DateField("deadline", auto_now=True)
    info = models.CharField("information", max_length=1000)

    def get_responses(self):
        return ApplicationResponse.objects.filter(answers__question__form=self).distinct()

class Question(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['form', 'number'], name='unique_form_number')]

    form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField("question", max_length=QUESTION_MAX_LENGTH)
    number = models.IntegerField()
    type = models.CharField("type", max_length=255)

    def save(self, *args, **kwargs):
        self.type = self.__class__.__name__
        super().save(*args, **kwargs)

    def typed(self):
        if self.type:
            return self.__getattribute__(self.type.lower())
        else:
            return self

    def make_answer(self):
        raise NotImplementedError

    def __str__(self):
        return self.question



class ApplicationResponse(models.Model):
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='responses')
    date = models.DateField("date_submitted", auto_now=True)
    state = models.CharField(max_length=1, choices=APPLICATION_STATES)

    def get_form(self):
        return self.answers.first().question.form
    # todo
    # constraints = for all answer in self.answers answer.question.form should be the same


class Answer(models.Model):
    response = models.ForeignKey(ApplicationResponse, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    type = models.CharField("type", max_length=255)

    def save(self, *args, **kwargs):
        self.type = self.__class__.__name__
        super().save(*args, **kwargs)

    def typed(self):
        if self.type:
            return self.__getattribute__(self.type.lower())
        else:
            return self

class TextualQuestion(Question):
    def make_answer(self):
        t = TextualAnswer()
        t.question = self
        return t

class TextualAnswer(Answer):
    value = models.CharField('text_value', max_length=100, default="")
    def __str__(self):
        return self.value

class MultiChoiceQuestion(Question):
    def make_answer(self):
        t = MultiChoiceAnswer()
        t.question = self

class MultiChoiceAnswer(Answer):
    value = models.CharField("choice_value", max_length=CHOICE_MAX_LENGTH)

    def __str__(self):
        return self.value


class NumericalQuestion(Question):
    def make_answer(self):
        t = NumericalAnswer()
        t.question = self
        return t

class NumericalAnswer(Answer):
    value = models.IntegerField('int_value')

    def __str__(self):
        return str(self.value)
