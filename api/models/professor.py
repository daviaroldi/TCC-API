from django.db import models
from django.contrib.auth.models import User

class Professor(User):
    def is_professor(self):
        return True
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')