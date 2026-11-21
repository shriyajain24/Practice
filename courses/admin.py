from django.contrib import admin
from .models import (
    Subject, SyllabusTopic, StudyMaterial, 
    Assignment, Submission, Quiz, Question, Option, QuizAttempt
)
from accounts.models import Department, Program, Semester, CustomUser

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Semester)
admin.site.register(CustomUser)
admin.site.register(Subject)
admin.site.register(SyllabusTopic)
admin.site.register(StudyMaterial)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QuizAttempt)