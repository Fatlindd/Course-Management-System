from django.test import TestCase
from django.urls import reverse
from courses.models import Course
from courses.forms import CourseForm


class TestStudentViews(TestCase):
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
            name='Python',
            start_date='2023-06-12',
            price=320,
            image='images/course2.png',
            notes='Python Programming Language'
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:home'))
        self.assertTemplateUsed(response, 'courses/home.html')
        self.assertContains(response, self.course1.name)
        self.assertContains(response, self.course2.name)
        self.assertContains(response, self.course1.price)
        self.assertContains(response, self.course2.price)
        self.assertIn(self.course1, response.context['course_list'])
        self.assertContains(response, self.course2.notes)

    def test_course_create_view(self):
        course_data = {
            'name': 'JavaScript',
            'price': 260,
            'image': 'images/javascript.com',
            'start_date': '2023-07-10',
            'notes': 'JavaScript Coding'
        }
        response = self.client.post(reverse('courses:add_course'), course_data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIsInstance(form, CourseForm)
        self.assertContains(response, 'name')
        self.assertContains(response, 'start_date')
        self.assertContains(response, 'notes')

    def test_course_detail_view(self):
        response = self.client.get(reverse('courses:view_course', args=[self.course1.pk]))
        self.assertTemplateUsed(response, 'courses/view_course.html')
        self.assertContains(response, self.course1.name)
        self.assertNotContains(response, f"{self.course2.price}€")

    def test_course_edit_view(self):
        course_data = {
                'name': 'React',
                'price': 250,
                'image': 'images/react.com',
                'start_date': '2023-07-10',
                'notes': 'React Coding'
            }

        response = self.client.post(reverse('courses:edit_course', args=[self.course2.pk]), data=course_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('courses:home'))
        self.assertTrue(Course.objects.filter(name='React').exists())

    def test_course_delete_view(self):
        response = self.client.get(reverse('courses:delete_course', args=[self.course2.pk]))
        self.assertContains(response, 'Are you sure you want to delete this course?')
        self.assertContains(response, self.course2.name)
        self.assertTemplateUsed(response, 'courses/delete_course.html')

        response = self.client.post(reverse('courses:delete_course', args=[self.course2.pk]))
        self.assertFalse(Course.objects.filter(pk=self.course2.pk).exists())
