from django.urls import path
from teachers.views import TeacherListView, TeacherCreateView, TeacherDetailView, TeacherDeleteView, TeacherUpdateView

app_name = 'teachers'
urlpatterns = [
    path('home/', TeacherListView.as_view(), name='home'),
    path('add_teacher/', TeacherCreateView.as_view(), name='add_teacher'),
    path('detail_teacher/<int:pk>/', TeacherDetailView.as_view(), name='detail_teacher'),
    path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher'),
    path('edit_teacher/<int:pk>/', TeacherUpdateView.as_view(), name='edit_teacher'),
]
