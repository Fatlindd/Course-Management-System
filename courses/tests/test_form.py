from django.test import TestCase
from courses.forms import CourseForm


class TestCourseForm(TestCase):
    def test_valid_data(self):
        form = CourseForm({
            'name': 'Django',
            'price': 270.00,
            'image': 'images/image.jpg',
            'start_date': '2023-05-20',
            'notes': 'Django is Python Framework'
        })
        self.assertTrue(form.is_valid())

    def test_missing_required_field(self):
        form = CourseForm({
            'price': 270.00,
            'image': 'path/to/image.jpg',
            'start_date': '2023-05-20',
            'notes': 'Django is Python Framework'
        })
        self.assertFalse(form.is_valid())

    def test_invalid_data(self):
        form = CourseForm({
            'name': 'Django',
            'price': 'not a number',
            'image': 'path/to/image.jpg',
            'start_date': '2023-05-20',
            'notes': 'Django is Python Framework'
        })
        self.assertFalse(form.is_valid())
