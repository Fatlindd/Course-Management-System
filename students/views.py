from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Student
from courses.models import Course
from teachers.models import Teacher
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if not request.session.get('user'):
        return redirect(reverse('users:login'))
    courses = Course.objects.all()
    teachers = Teacher.objects.all()

    column = request.GET.get('column')
    query = request.GET.get('query')
    if not column or column == 'all':
        students = Student.objects.all()
    elif column == 'first_name':
        students = Student.objects.filter(first_name__icontains=query)
    elif column == 'last_name':
        students = Student.objects.filter(last_name__icontains=query)
    elif column == 'age':
        students = Student.objects.filter(age=query)
    elif column == 'email':
        students = Student.objects.filter(email__icontains=query)
    elif column == 'course':
        students = Student.objects.filter(course__name__icontains=query)
    elif column == 'teacher':
        students = Student.objects.filter(teacher__first_name__icontains=query)

    return render(request, 'students/home.html', {'students': students, 'teachers': teachers, 'courses': courses})


def view_student(request, pk):
    student = Student.objects.get(pk=pk)
    if student:
        return render(request, 'students/view_student.html', {'student': student})


def add_student(request):
    if request.method == 'POST':
        error_messages = {}

        first_name = request.POST.get('first_name')
        if not first_name:
            error_messages['error_first_name'] = 'Field First Name is required!'

        last_name = request.POST.get('last_name')
        if not last_name:
            error_messages['error_last_name'] = 'Field Last Name is required!'

        age = request.POST.get('age')
        if not age:
            error_messages['error_age'] = 'Field Age is required!'

        email = request.POST.get('email')

        if email and Student.objects.filter(email=email).exists():
            error_messages['email_exists'] = "A student with the same email already exists."

        if not email:
            error_messages['email_error'] = 'Field email is required!'

        gender = request.POST.get('gender')
        if not gender:
            error_messages['gender_error'] = 'Field gender is required!'
        
        course = request.POST.get('course')
        if not course:
            error_messages['course_error'] = 'Field course is required!'

        teacher = request.POST.get('teacher')
        if not teacher:
            error_messages['teacher_error'] = 'Field teacher is required!'

        if error_messages:
            return render(request, 'students/add_student.html', error_messages)
        else:
            course_id = request.POST.get('course')
            course = Course.objects.get(pk=course_id)
            teacher_id = request.POST.get('teacher')
            teacher = Teacher.objects.get(pk=teacher_id)
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                email=email,
                gender=gender,
                course=course,
                teacher=teacher
            )
            messages.success(request, 'Student added successfully!')
        return redirect('students:home')
    elif request.method == 'GET':
        return render(request, 'students/add_student.html', {'teachers': Teacher.objects.all(), 'courses': Course.objects.all()})


def delete_student(request, pk):
    if request.method == "POST":
        student = get_object_or_404(Student, pk=pk)
        student.delete()
    return HttpResponseRedirect(reverse('students:home'))


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    teachers = Teacher.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.course.pk = request.POST.get('course')
        student.course = Course.objects.get(pk=student.course.pk)

        student.save()
        return HttpResponseRedirect(reverse('students:home'))
