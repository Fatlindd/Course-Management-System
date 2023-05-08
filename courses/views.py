from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Course
from .forms import CourseForm


class CourseListView(ListView):
    model = Course
    template_name = 'courses/home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect(reverse('users:login'))
        return super().dispatch(request, *args, **kwargs)


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/add_course.html'
    success_url = reverse_lazy('courses:home')


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/view_course.html"


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/edit_course.html'
    success_url = reverse_lazy('courses:home')
    

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/delete_course.html'
    success_url = reverse_lazy("courses:home")


