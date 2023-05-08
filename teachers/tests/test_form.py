from django.test import TestCase
from teachers.forms import TeacherForm
from courses.models import Course
from teachers.models import Teacher


class TeacherFormTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Django',
            start_date='2023-05-20',
            price=270.00,
            notes='Django is Python Framework'
        )

    def test_teacher_form_valid(self):
        form_data = {
            'first_name': 'Ali',
            'last_name': 'Gashi',
            'age': 49,
            'email': 'ali.gashi@gmail.com',
            'course': self.course.pk,
        }
        form = TeacherForm(data=form_data)
        self.assertTrue(form.is_valid())
        teacher = form.save()
        self.assertEqual(teacher.first_name, 'Ali')
        self.assertEqual(teacher.last_name, 'Gashi')
        self.assertEqual(teacher.age, 49)
        self.assertEqual(teacher.email, 'ali.gashi@gmail.com')
        self.assertEqual(teacher.course, self.course)

    def test_teacher_form_invalid(self):
        form_data = {
            'first_name': 'Ali',
            'last_name': 'Gashi',
            'age': '42',
            'email': 'invalid-email',
            'course': self.course.pk,
        }
        form = TeacherForm(data=form_data)
        self.assertFalse(form.is_valid())
