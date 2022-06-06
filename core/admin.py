# core.admin.py

from django.contrib import admin

from core.models import choice, question

admin.site.register(choice.Choice)
admin.site.register(question.Question)
