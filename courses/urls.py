from django.urls import path
from .views import CourseListView, CourseCreateView, CourseDeleteView, CourseUpdateView, CourseDetailView

app_name = 'courses'
urlpatterns = [
    path('home/', CourseListView.as_view(), name='home'),
    path('add_course/', CourseCreateView.as_view(), name='add_course'),
    path('delete_course/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),
    path('edit_course/<int:pk>/', CourseUpdateView.as_view(), name='edit_course'),
    path('view_course/<int:pk>/', CourseDetailView.as_view(), name="view_course"),
]
