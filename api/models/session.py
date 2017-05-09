from django.db import models
from .professor import Professor
from .student import Student

import os
from binascii import hexlify

class Session(models.Model):
    code = models.CharField(max_length=10, unique=True)
    deadline = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)

    def save(self, *args, **kwargs):
        code = hexlify(os.urandom(5))
        self.code = code
        super(Session, self).save(*args, **kwargs)

        # ef
        # _createHash():
        # """This function generate 10 character long hash"""
        # return hexlify(os.urandom(5))
