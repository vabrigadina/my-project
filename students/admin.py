

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'program', 'course', 'group_number', 'specialization', 'graduation_year', 'average_grade']
    search_fields = ['full_name', 'program', 'group_number']