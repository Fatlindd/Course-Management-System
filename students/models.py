from django.db import models
from courses.models import Course
from teachers.models import Teacher


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    gender_choice = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=gender_choice)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='students', null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='students', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'Student'

