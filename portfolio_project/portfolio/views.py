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

from django.core.mail import send_mail
from django.conf import settings
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка на вашу почту
        send_mail(
            f"Новое сообщение от {name}",
            f"Имя: {name}\nEmail: {email}\n\nСообщение:\n{message}",
            settings.DEFAULT_FROM_EMAIL,  # Ваш email в settings.py
            ['emelyanov2704@mail.ru'],  # Куда отправлять
            fail_silently=False,
        )

        return redirect('success_page')  # Перенаправление после отправки

    return render(request, 'portfolio/home.html')