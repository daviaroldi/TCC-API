from django.db import models
from .question import Question

class Option(models.Model):
    label = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='options')
