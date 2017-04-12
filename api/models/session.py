from django.db import models
from .professor import Professor
from .student import Student

class Session(models.Model):
    code = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    student = models.ManyToManyField(Student)