from django.test import TestCase
from teachers.models import Teacher
from courses.models import Course


class TestTeacherModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course1 = Course.objects.create(
            name='Django',
            start_date='2023-05-20',
            price=270.00,
            notes='Django is Python Framework'
        )
        cls.teacher1 = Teacher.objects.create(
            first_name='Ali',
            last_name='Gashi',
            age=49,
            email='ali.gashi@gmail.com',
            course=cls.course1,
        )

    def test_teacher_data(self):
        self.assertEqual(str(self.teacher1), 'Ali Gashi')
        self.assertEqual(self.teacher1.first_name, 'Ali')
        self.assertEqual(self.teacher1.course, self.course1)
        self.assertEqual(self.teacher1.age, 49)
        self.assertNotEquals(self.teacher1.last_name, 'Krasniqi')