from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
  path('home/', views.home, name='home'),
  path('add_student/', views.add_student, name='add_student'),
  path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
  path('view_student/<int:pk>/', views.view_student, name='view_student'),
  path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
]


