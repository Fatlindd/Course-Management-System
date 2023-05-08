from django.test import TestCase
from django.urls import reverse
from courses.models import Course


class TestCourseUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course1 = Course.objects.create(
            name='Django',
            start_date='2023-05-20',
            price=270.00,
            image='images/course1.png',
            notes='Django is Python Framework'
        )

        cls.course2 = Course.objects.create(
            name='Java',
            start_date='2023-06-12',
            price=310,
            image='images/course2.png',
            notes='Java Programming Language'
        )

    def test_url_for_home(self):
        response = self.client.get(reverse('courses:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/home.html')

    def test_url_for_add_course(self):
        response = self.client.get(reverse('courses:add_course'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/add_course.html')

    def test_url_for_delete_course(self):
        response = self.client.get(reverse('courses:delete_course', args=[self.course1.pk]))
        self.assertEqual(response.status_code, 200)

    def test_url_for_edit_course(self):
        response = self.client.get(reverse('courses:edit_course', args=[self.course1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/edit_course.html')

    def test_url_for_view_course(self):
        response = self.client.get(reverse('courses:view_course', args=[self.course2.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/view_course.html')
