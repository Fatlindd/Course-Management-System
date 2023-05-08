from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'email', 'course']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'email': 'Email',
            'course': 'Course'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name...'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your age...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email...'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }
