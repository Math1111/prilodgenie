from django.contrib import admin
from .models import Project, Skill, ContactRequest

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ContactRequest)