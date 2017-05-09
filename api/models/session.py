from django.db import models
from .professor import Professor
from .student import Student

class Session(models.Model):
    code = models.AutoField(primary_key=False)
    deadline = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)

    def save(self, *args, **kwargs):
        # self.code =
        super(Session, self).save(*args, **kwargs)