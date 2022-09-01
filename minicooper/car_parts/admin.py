from django.contrib import admin
from .models import (
	CarPart,
	CarPartCar
	)

# Register your models here.
@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
	list_display = ('part_name', 'part_price',)

@admin.register(CarPartCar)
class CarPartCarAdmin(admin.ModelAdmin):
	list_display = ('car_part', 'car',)