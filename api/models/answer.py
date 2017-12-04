from django.db import models
from .option import Option
from .student import Student
from .question import Question

class Answer(models.Model):
    value = models.TextField()
    option = models.ForeignKey(Option, on_delete=models.DO_NOTHING, related_name='answer', null=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answers', null=True)