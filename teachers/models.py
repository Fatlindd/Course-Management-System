from django.db import models
from courses.models import Course


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def num_students(self):
        return self.course.students.count()

    class Meta:
        db_table = 'Teacher'