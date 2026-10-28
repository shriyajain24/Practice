from django.db import models
from django.contrib.auth.models import User
import os
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.


# Semester
class Semester(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name



# Subject
class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.code})"



# SyllabusTopic
class SyllabusTopic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject.code} - {self.title}"
    
    

# Validation of study material 
def validate_study_material_file(file):
    
    max_size_mb = 10
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size cannot exceed {max_size_mb}MB.")
    
    
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.pdf', '.ppt', '.pptx', '.doc', '.docx']
    if ext not in valid_extensions:
        raise ValidationError("Only PDF, PPT, and DOC files are allowed.")
    
    
    
# Study Material (Digital Library)
class StudyMaterial(models.Model):
    MATERIAL_TYPES = [
        ('NOTES', 'Notes'),
        ('PPT', 'PPT Presentation'),
        ('PYQ', 'Previous Year Questions'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPES, default='NOTES')
    file = models.FileField(upload_to='study_materials/', validators=[validate_study_material_file])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_material_type_display()}) - {self.subject.code}"
    
    
    
    
# Assignment Model(Faculty)
class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.subject.code}"
    
    
    

# Submission (Student):
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_late = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        if timezone.now() > self.assignment.deadline:
            self.is_late = True
        else:
            self.is_late = False
        super().save(*args, **kwargs)

    def __str__(self):
        status = "Late" if self.is_late else "On Time"
        return f"{self.student.username} - {self.assignment.title} ({status})"



# Online MCQ Quiz :
# 1. Quiz Model

