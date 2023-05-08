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

    def test_view_student(self):
        response = self.client.get(reverse('students:view_student', args=[self.student.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/view_student.html') 
        self.assertContains(response, 'First Name:')

    def test_add_student_view(self):
        student_data = {
            'first_name': 'Fatlind',
            'last_name': 'Thaci',
            'age': 25,
            'email': 'fatlindthaci@gmail.com',
            'gender': 'M',
            'course': self.course.pk,
            'teacher': self.teacher.pk
        }
        response = self.client.post(reverse('students:add_student'), data=student_data)
        self.assertEqual(response.status_code, 302) # 302 is used to check if user redirect after form
        self.assertTrue(Student.objects.filter(first_name='Fatlind').exists())
        self.assertRedirects(response, reverse('students:home'))

        response = self.client.post(reverse('students:add_student'), {})
        self.assertTemplateUsed(response, 'students/add_student.html')

    def test_delete_student_view(self):
        response = self.client.post(reverse('students:delete_student', args=[self.student.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(first_name='Fatlind').exists())
        self.assertRedirects(response, reverse('students:home'))
    
    def test_edit_student_view(self):
        student_data = {
            'first_name': 'Fatlind',
            'last_name': 'Thaci',
            'age': 24,
            'email': 'fatlindthaci@gmail.com',
            'gender': 'M',
            'course': self.course.pk,
            'teacher': self.teacher.pk
        }
        response = self.client.post(reverse('students:edit_student', args=[self.student.pk]), data=student_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(age=24).exists())
        self.assertRedirects(response, reverse('students:home'))

        # response = self.client.post(reverse('students:edit_student', args=[self.student.pk]))
        # self.assertTemplateUsed(response, 'students/edit_student.html')