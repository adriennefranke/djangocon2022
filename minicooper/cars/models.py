from django.db import models
from datetime import datetime

# Create your models here.
YEAR_CHOICES = []
for i in range(1969, datetime.now().year):
	choice = (i, str(i))
	YEAR_CHOICES.append(choice)

class Car(models.Model):
	model_name = models.CharField("Model Name", max_length=255, blank=False)
	year_released = models.IntegerField("Year Released", choices=YEAR_CHOICES)
	msrp = models.DecimalField("MSRP", max_digits=8, decimal_places=2)

	def __str__(self):
		return f'{self.year_released} {self.model_name}'

