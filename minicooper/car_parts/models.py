from django.db import models
from cars.models import Car

# Create your models here.
class CarPart(models.Model):
	part_name = models.CharField("Part Name", max_length=255, blank=False)
	part_price = models.DecimalField("Part Price", max_digits=8, decimal_places=2)

	admin_help_text = "Use this page to adjust the price of a car part."

	class Meta:
		verbose_name = "Car Part"

	def __str__(self):
		return f'{self.part_name}'

class CarPartCar(models.Model):
	car_part = models.ForeignKey("CarPart", verbose_name="Car Part", on_delete=models.PROTECT)
	car = models.ForeignKey(Car, on_delete=models.PROTECT)

	class Meta:
		verbose_name = "Car Parts Car"