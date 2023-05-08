from django.test import TestCase
from django.urls import reverse
from students.models import Student
from courses.models import Course
from teachers.models import Teacher


class TestStudentUrls(TestCase):
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

    def test_url_for_home(self):
            response = self.client.get(reverse('students:home'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'students/home.html')

    def test_url_for_add_student(self):
        response = self.client.get(reverse('students:add_student'))
        self.assertEqual(response.status_code, 200)

    def test_url_for_delete_student(self):
         response = self.client.post(reverse('students:delete_student', args=[self.student.pk]))
         self.assertEqual(response.status_code, 302)
         
    def test_url_for_view_student(self):
        response = self.client.get(reverse("students:view_student", args=[self.student.pk]))
        self.assertEqual(response.status_code, 200)
        

