from django.db import models
from .session import Session

class Question(models.Model):
    description = models.EmailField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)