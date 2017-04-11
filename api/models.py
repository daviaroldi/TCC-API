from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    alt = models.CharField(max_length=255)
    gender = models.CharField(max_length=30)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Session(models.Model):
    code = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)

class Question(models.Model):
    description = models.EmailField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Answer(models.Model):
    value = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
