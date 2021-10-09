from django.db import models

# Create your models here.

class Student(models.Model):
    student_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    student_dob = models.DateField(null=True, blank=True)
    student_doj = models.DateField(null=True, blank=True)