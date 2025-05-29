from django.shortcuts import render
from .models import AboutMe, EducationalProgram, Management, Classmate

def about_me_view(request):
    about = AboutMe.objects.first()
    return render(request, 'hse_site/about_me.html', {'about': about})

def educational_program(request):
    program = EducationalProgram.objects.first()
    return render(request, 'hse_site/educational_program.html', {'program': program})

def management(request):
    management = Management.objects.first()
    return render(request, 'hse_site/management.html', {'management': management})

def classmates(request):
    classmates = Classmate.objects.all()
    # Фильтрация по начальной русской букве имени
    letter = request.GET.get('letter', '')
    if letter:
        classmates = classmates.filter(name__istartswith=letter)
    # Сортировка по email с возможностью переключения направления
    sort_order = request.GET.get('sort_order', 'asc')  # 'asc' или 'desc'
    if sort_order == 'desc':
        classmates = classmates.order_by('-email')
    else:
        classmates = classmates.order_by('email')
    return render(request, 'hse_site/classmates.html', {'classmates': classmates, 'letter': letter, 'sort_order': sort_order})