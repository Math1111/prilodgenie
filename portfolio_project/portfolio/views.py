from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Skill, ContactRequest
from django.contrib import messages

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactRequest.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)