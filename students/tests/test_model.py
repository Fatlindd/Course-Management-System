# Execute this: python manage.py test students.tests.test_model
from django.test import TestCase
from django.urls import reverse
from students.models import Student
from courses.models import Course
from teachers.models import Teacher


class TestStudentModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course = Course.objects.create(name='Python', start_date='2023-06-14', price=250.00)
        cls.teacher = Teacher.objects.create(first_name='Filan', last_name='Fisteku', age=40, course=cls.course)
        cls.student = Student.objects.create(
            first_name='Fatlind',
            last_name='Thaci',
            age=24,
            email='fatlind.thaci@gmail.com',
            gender='M',
            course=cls.course,
            teacher=cls.teacher
        )

    def test_student_data(self):
        self.assertEqual(str(self.student), 'Fatlind Thaci')
        self.assertEqual(self.student.teacher.first_name, 'Filan')
        self.assertEqual(self.student.course.name, 'Python')
        self.assertEqual(self.student.course.price, 250.00)
        self.assertEqual(self.student.email, 'fatlind.thaci@gmail.com')
    
    
    