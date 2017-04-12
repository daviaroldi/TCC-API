from django.db import models
from .user import User

class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)