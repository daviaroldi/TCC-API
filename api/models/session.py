from django.db import models
from .professor import Professor
from .student import Student
from django.utils import timezone

import os
from binascii import hexlify

class Session(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)

    def save(self, *args, **kwargs):
        code = hexlify(os.urandom(5))
        self.code = code
        super(Session, self).save(*args, **kwargs)

    def is_open(self):
        return True #self.deadline > timezone.now()
