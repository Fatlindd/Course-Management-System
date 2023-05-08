from django.test import TestCase
from courses.models import Course


class TestCourseModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course1 = Course.objects.create(
            name='Django',
            start_date='2023-05-20',
            price=270.00,
            notes='Django is Python Framework'
        )

        cls.course2 = Course.objects.create(
            name='Java',
            start_date='2023-06-12',
            price=310,
            notes='Java Programming Language'
        )

    def test_course_data(self):
        self.assertEqual(str(self.course1), self.course1.name)
        self.assertEqual(str(self.course2), 'Java')
        self.assertEqual(self.course1.name, 'Django')
        self.assertEqual(self.course1.start_date, '2023-05-20')
        self.assertEqual(self.course1.price, 270.00)
        self.assertEqual(self.course2.notes, 'Java Programming Language')
