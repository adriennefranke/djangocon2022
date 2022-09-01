from django.db import models
from cars.models import Car

# Create your models here.
class Sale(models.Model):
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	sale_price = models.DecimalField("Sale Price", max_digits=8, decimal_places=2)
	sale_date = models.DateTimeField("Sale Date")

