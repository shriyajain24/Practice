from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.dept_name} ({self.dept_code})"


class Program(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=50)
    program_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.program_name} ({self.program_code})"


class Semester(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester_number = models.IntegerField()
    semester_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.semester_name


class CustomUser(models.Model):
    uid = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=80, unique=True, null=False)

    ROLES_CHOICE = [
        ('Faculty', 'FACULTY'),
        ('Admin', 'ADMIN'),
        ('Student', 'STUDENT')
    ]
    role = models.CharField(max_length=50, choices=ROLES_CHOICE, default="Student")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.uid})"