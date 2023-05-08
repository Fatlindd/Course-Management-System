from django.test import TestCase
from django.urls import reverse
from courses.models import Course
from teachers.models import Teacher
from teachers.forms import TeacherForm
from django.template.loader import select_template


class TestTeacherViews(TestCase):
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
    
    def test_teacher_list_view(self):
        response = self.client.get(reverse('teachers:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ali')
        self.assertContains(response, 'Django')
        self.assertContains(response, 'Gashi')
        self.assertContains(response, 'Course')
        self.assertQuerysetEqual(response.context['teacher_list'], ['<Teacher: Ali Gashi>'])
    
    def test_create_teacher(self):
        teacher2 = {
            'first_name': 'Fatlind',
            'last_name': 'Thaci',
            'age': 24,
            'email': 'fatlindthaci@gmail.com',
            'course': self.course1.pk
        }
        response = self.client.post(reverse('teachers:add_teacher'), teacher2)
        self.assertRedirects(response, reverse('teachers:home'))
        
        # Check if the teacher has been added to the database
        teachers = Teacher.objects.filter(first_name='Fatlind', last_name='Thaci')
        teacher = teachers.first()
        self.assertEqual(teacher.first_name, 'Fatlind')
        self.assertEqual(teacher.last_name, 'Thaci')
        self.assertEqual(teacher.age, 24)
        self.assertEqual(teacher.email, 'fatlindthaci@gmail.com')
        self.assertEqual(teacher.course, self.course1)
    
    def test_teacher_detail_view(self):
        response = self.client.get(reverse('teachers:detail_teacher', args=[self.teacher1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "detail_teacher.html")
        self.assertContains(response, "First Name:")
        self.assertContains(response, "Last Name:")
        self.assertContains(response, "Age:")
        self.assertContains(response, "Email:")
        self.assertContains(response, "Course:")
        self.assertContains(response, "Students nr:")
    
    def test_teacher_edit_view(self):
        response = self.client.get(reverse('teachers:edit_teacher', kwargs={'pk': self.teacher1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/edit_teacher.html')
        self.assertIsInstance(response.context['form'], TeacherForm)
        
        new_data = {
            'first_name': 'Fatlon',
            'last_name': 'Thaci',
            'age': 30,
            'email': 'fatlonthaci@gmail.com',
            'course': self.course1.pk,
        }
        
        response = self.client.post(reverse('teachers:edit_teacher', kwargs={'pk': self.teacher1.pk}), data=new_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('teachers:home'))
        
        # is used to refresh the object's attributes with the most recent data from the database. 
        self.teacher1.refresh_from_db()
        self.assertEqual(self.teacher1.first_name, 'Fatlon')
        self.assertEqual(self.teacher1.last_name, 'Thaci')
        self.assertEqual(self.teacher1.age, 30)
        self.assertEqual(self.teacher1.email, 'fatlonthaci@gmail.com')
        self.assertEqual(self.teacher1.course, self.course1)
    
    def test_teacher_delete_view(self):
        response = self.client.post(reverse("teachers:delete_teacher", kwargs={"pk": self.teacher1.pk}))
        self.assertEqual(response.status_code, 302)
        # check that the teacher was deleted
        self.assertFalse(Teacher.objects.filter(pk=self.teacher1.pk).exists()) 
