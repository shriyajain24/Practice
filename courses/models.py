from django.db import models



# Create your models here.

class Semester(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
