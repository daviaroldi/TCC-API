from django.db import models
from .session import Session

class Question(models.Model):
    description = models.TextField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='questions')