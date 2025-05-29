from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'program', 'course', 'group_number', 'specialization', 'graduation_year', 'average_grade']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Иванов Иван Иванович'}),
            'program': forms.TextInput(attrs={'placeholder': 'Иностранные языки'}),
            'course': forms.Select(),
            'group_number': forms.TextInput(attrs={'placeholder': '244'}),
            'specialization': forms.Select(),
            'graduation_year': forms.NumberInput(attrs={'placeholder': '2025'}),
            'average_grade': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '10'}),
        }