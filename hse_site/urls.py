from django.urls import path
from . import views

app_name = 'hse_site'

urlpatterns = [
    path('about_me/', views.about_me_view, name='about_me'),
    path('educational_program/', views.educational_program, name='educational_program'),
    path('management/', views.management, name='management'),
    path('classmates/', views.classmates, name='classmates'),
]