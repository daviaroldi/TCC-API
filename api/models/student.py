from django.db import models

from django.contrib.auth.models import User

class Student(User):
    def is_professor(self):
        return False
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="users")
