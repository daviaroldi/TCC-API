from django.db import models
from .professor import Professor
from .student import Student
# from .question import Question
from datetime import datetime
import time
from django.utils import timezone
import pytz

import os
from binascii import hexlify

class Session(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    started_at = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)

    def save(self, *args, **kwargs):
        code = hexlify(os.urandom(5))
        self.code = code
        super(Session, self).save(*args, **kwargs)

    def is_open(self):
        utc = pytz.timezone('America/Sao_Paulo')
        timezone.activate(utc)
        now = timezone.now()
        now = now.replace(tzinfo=utc)
        now = now.astimezone(utc)
        print(time.localtime())

        datetime_start = self.deadline
        datetime_end = self.started_at
        if datetime_start.tzinfo is None:
            datetime_start = utc.localize(self.started_at)
        if datetime_end.tzinfo is None:
            datetime_end = utc.localize(self.deadline)
        return datetime_end > now and datetime_start < now
