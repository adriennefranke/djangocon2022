from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ('model_name', 'year_released', 'msrp')
	search_fields = ('model_name', 'year_released')