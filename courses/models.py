from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Semester(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.code})"




class SyllabusTopic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject.code} - {self.title}"