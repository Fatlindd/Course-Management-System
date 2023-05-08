from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'price', 'image', 'start_date', 'notes']
        labels = {
            'name': 'Name',
            'price': 'Price',
            'image': 'Image',
            'notes': 'Notes',
            'start_date': 'Start Date'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Course price...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'cols': 5, 'rows': 5, 'placeholder': 'Description for course...'}),
        }
