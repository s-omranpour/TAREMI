from django.db import models

from broker.constants import *


class ApplicationForm(models.Model):
    name = models.CharField("Name", max_length=NAME_LENGTH)
    # creator = foreignkey

class MultiChoiceQuestion(models.Model):
    form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)

class TextualQuestion(models.Model):
    form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)
    answer = models.CharField("Answer", max_length=ANSWER_MAX_LENGTH)

class NumericalQuestion(models.Model):
    form = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE, related_name="textual_questions")
    question = models.CharField("Question", max_length=QUESTION_MAX_LENGTH)
    answer = models.IntegerField("Answer", max_length=ANSWER_MAX_LENGTH)

class Choice(models.Model):
    value = models.CharField("Value", max_length=CHOICE_MAX_LENGTH)
    question = models.ForeignKey(MultiChoiceQuestion, on_delete=models.CASCADE)
