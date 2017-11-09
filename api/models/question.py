from django.db import models
from .session import Session
# from .type import Type

class Question(models.Model):
    description = models.TextField()
    type = models.IntegerField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='questions')