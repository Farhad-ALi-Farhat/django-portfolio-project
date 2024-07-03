from django.shortcuts import render
from .models import Education, Skill, Experience, Project

def home(request):
    context = {
        'education': Education.objects.all(),
        'skills': Skill.objects.all(),
        'experience': Experience.objects.all(),
        'projects': Project.objects.all(),
    }
    return render(request, 'core/home.html', context)

def contact_form_view(request):
    # View logic for handling the contact form
    return render(request, 'core/contact_form.html')