from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .forms import TeacherForm
from .models import Teacher


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect(reverse('users:login'))
        return super().dispatch(request, *args, **kwargs)


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/add_teacher.html'
    success_url = reverse_lazy('teachers:home')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "detail_teacher.html"


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'detail_teacher.html'
    success_url = reverse_lazy("teachers:home")


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/edit_teacher.html'
    success_url = reverse_lazy('teachers:home')

