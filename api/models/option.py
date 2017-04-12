from django.db import models
from .question import Question

class Option(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
