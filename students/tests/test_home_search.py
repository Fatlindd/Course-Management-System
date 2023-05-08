from django.test import TestCase, client
from django.urls import reverse
from students.models import Student
from courses.models import Course
from teachers.models import Teacher


class TestHomeSearchView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course1 = Course.objects.create(name='Python', start_date='2023-06-14', price=120.00)
        cls.course2 = Course.objects.create(name='JavaScript', start_date='2023-08-23', price=190.00)
        cls.teacher1 = Teacher.objects.create(first_name='Filan', last_name='Fisteku', age=34, course=cls.course1)
        cls.teacher2 = Teacher.objects.create(first_name='Fatlind', last_name='Thaci', age=28, course=cls.course2)
        cls.student1 = Student.objects.create(
            first_name='Fatlon', 
            last_name='Thaci', 
            age=18, 
            email='fatlonthaci@gmail.com',
            course=cls.course1,
            teacher=cls.teacher1)
        cls.student2 = Student.objects.create(
            first_name='Blinera', 
            last_name='Hoxha', 
            age=20, 
            email='blinerahoxha@gmail.com',
            course=cls.course2,
            teacher=cls.teacher2)

    def test_search_by_all(self):
        response = self.client.get(reverse('students:home'), {'column': 'all', 'query': 'Fatlon'})
        self.assertContains(response, 'Fatlon Thaci')
        self.assertContains(response, 'fatlonthaci@gmail.com')

    def test_search_by_first_name(self):
        response = self.client.get(reverse('students:home'), {'column': 'first_name', 'query': 'Blinera'})
        self.assertContains(response, 'Blinera Hoxha')
        self.assertContains(response, 'blinerahoxha@gmail.com')
        self.assertNotContains(response, 'blinera.hoxha@gmail.com')

    def test_search_by_last_name(self):
        response = self.client.get(reverse('students:home'), {'column': 'last_name', 'query': 'Thaci'})
        self.assertContains(response, 'Fatlon Thaci')
        self.assertContains(response, 'fatlonthaci@gmail.com')
        self.assertNotContains(response, 'fatlon_thaci@gmail.com')

    def test_search_by_email(self):
        response = self.client.get(reverse('students:home'), {'column': 'email', 'query': 'blinerahoxha@gmail.com'})
        self.assertContains(response, 'JavaScript')
        self.assertNotContains(response, 'blinera.hoxha@gmail.com')

    def test_search_by_course(self):
        response1 = self.client.get(reverse('students:home'), {'column': 'course', 'query': 'python'})
        self.assertContains(response1, 'Fatlon')
        self.assertNotContains(response1, 'Blinera')

        response2 = self.client.get(reverse('students:home'), {'column': 'course', 'query': 'javascript'})
        self.assertContains(response2, 'Blinera')
        self.assertNotContains(response2, 'Fatlon')

    def test_search_by_teacher(self):
        response1 = self.client.get(reverse('students:home'), {'column': 'teacher', 'query': 'filan'})
        self.assertContains(response1, 'Filan Fisteku')
        self.assertContains(response1, 'Python')
        self.assertNotContains(response1, 'Filan Bytyci')

        response2 = self.client.get(reverse('students:home'), {'column': 'teacher', 'query': 'fatlind'})
        self.assertContains(response2, 'Fatlind Thaci')
        self.assertContains(response2, 'JavaScript')
        self.assertNotContains(response2, 'Fatlind Fisteku')
