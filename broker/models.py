from django.db import models

from broker.constants import *
from authentication.models import Instructor


class Application(models.Model):
    name = models.CharField("Name", max_length=NAME_LENGTH)
    creator = models.ForeingKey(Instructor, on_delete=models.CASCADE)
    release_date = models.DateField("release_date", auto_now=True)
    deadline = models.DateField("deadline", auto_now=True)


class MultiChoiceQuestion(models.Model):
    form = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)


class TextualQuestion(models.Model):
    form = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)
    answer = models.CharField("Answer", max_length=ANSWER_MAX_LENGTH)


class NumericalQuestion(models.Model):
    form = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)
    answer = models.IntegerField("Answer", max_length=ANSWER_MAX_LENGTH)


class Choice(models.Model):
    value = models.CharField("Value", max_length=CHOICE_MAX_LENGTH)
    question = models.ForeignKey(MultiChoiceQuestion, on_delete=models.CASCADE)
