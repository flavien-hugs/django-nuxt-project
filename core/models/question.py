# core.models.question.py

from datetime import datetime

from django.db import models
from django.conf import settings


class ActiveQuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
        	models.Q(
        		start_date__lte=datetime.now(),
        		end_date__gte=datetime.now()
        	)
        )


class ClosedQuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
        	end_date__lte=datetime.now()
        )


class Question(models.Model):
    owner = models.ForeignKey(
    	to=settings.AUTH_USER_MODEL,
    	on_delete=models.CASCADE
    )
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)

    objects = models.Manager()
    active = ActiveQuestionManager()
    closed = ClosedQuestionManager()

    def __str__(self) -> str:
        return self.text