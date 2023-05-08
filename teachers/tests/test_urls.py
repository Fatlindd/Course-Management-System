from django.test import TestCase
from django.urls import reverse
from teachers.models import Teacher
from courses.models import Course


class TestTeacherUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course1 = Course.objects.create(
            name='Math',
            start_date='2023-06-12',
            price=200,
            image='images/course2.png',
            notes='Java Programming Language'
        )

        cls.teacher1 = Teacher.objects.create(
            first_name='Blerim',
            last_name='Thaci',
            age=47,
            email='blerim.thaci@gmail.com',
            course=cls.course1,
        )
    
    def test_url_for_home(self):
        response = self.client.get(reverse('teachers:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/home.html')

    def test_url_for_add_teacher(self):
        response = self.client.get(reverse('teachers:add_teacher'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/add_teacher.html')
    
    def test_url_for_delete_teacher(self):
        response = self.client.post(reverse('teachers:delete_teacher', args=[self.teacher1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'teachers/delete_teacher.html')

    def test_url_for_edit_teacher(self):
        response = self.client.post(reverse('teachers:edit_teacher', args=[self.teacher1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/edit_teacher.html')
    
    def test_url_for_detail_teacher(self):
        response = self.client.get(reverse('teachers:detail_teacher', args=[self.teacher1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/detail_teacher.html')