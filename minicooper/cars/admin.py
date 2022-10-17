import decimal

from django.contrib import admin

from .models import Car


def increase_msrp_by_8_perc(modeladmin, request, queryset):
	for car in queryset:
		car.msrp = car.msrp * decimal.Decimal('1.08')
		car.save()
increase_msrp_by_8_perc.short_description = 'Increase MSRP by 8%%'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = ('model_name', 'year_released', 'msrp')
	search_fields = ('model_name', 'year_released')
	actions = [increase_msrp_by_8_perc, ]

