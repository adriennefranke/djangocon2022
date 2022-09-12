from django.contrib import admin
from django import forms
from .models import (
	CarPart,
	CarPartCar
	)

class CarPartForm(forms.ModelForm):

	expand_prices_to_cars_with_this_part = forms.BooleanField(required=False)

	class Meta:
		model = CarPart
		fields = '__all__'

	def clean(self):
		cleaned_data = super().clean()

		import pdb
		pdb.set_trace()

		car_part_id = self.instance.id
		car_part_price = cleaned_data.get('part_price')
		# cars_with_part = 1
		expand_prices_to_cars_with_this_part = cleaned_data.get('expand_prices_to_cars_with_this_part')

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
	form = CarPartForm
	
	def save_model(self, request, obj, form, change):
		if form.cleaned_data.get('expand_prices_to_cars_with_this_part'):
			# insert function here
			pass
		else:
			super().save_model(request, obj, form, change)



@admin.register(CarPartCar)
class CarPartCarAdmin(admin.ModelAdmin):
	list_display = ('car_part', 'car',)