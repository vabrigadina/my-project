from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Count

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def student_list(request):
    sort_by = request.GET.get('sort_by', 'full_name')
    specialization_filter = request.GET.get('specialization', '')
    students = Student.objects.all()
    
    if specialization_filter:
        students = students.filter(specialization=specialization_filter)
    
    students = students.order_by(sort_by)
    
    specializations = Student.SPECIALIZATION_CHOICES
    stats = Student.objects.values('specialization').annotate(count=Count('specialization'))
    stats_dict = {s['specialization']: s['count'] for s in stats}
    specialization_stats = [
        {'name': dict(specializations).get(s, s), 'count': stats_dict.get(s, 0)}
        for s in dict(specializations).keys()
    ]
    
    return render(request, 'students/student_list.html', {
        'students': students,
        'specializations': specializations,
        'selected_specialization': specialization_filter,
        'stats': specialization_stats,
    })