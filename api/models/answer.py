from django.db import models
from .option import Option
from .student import Student

class Answer(models.Model):
    value = models.TextField()
    option = models.ForeignKey(Option, on_delete=models.DO_NOTHING, null=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)