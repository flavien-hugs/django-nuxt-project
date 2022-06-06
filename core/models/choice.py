# core.models.choice.py

from django.db import models

from core.models.question import Question


class Choice(models.Model):
	question = models.ForeignKey(
		to=Question,
		on_delete=models.CASCADE,
		related_name="choices"
	)
	text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self) -> str:
		return self.text