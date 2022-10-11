from django.contrib import admin
from django import forms
from .models import (
	CarPart,
	CarPartCar
	)
from cars.models import Car

class CarPartForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		# This custom section changes the help_text for the expand_prices_to_cars_with_this_part field
		super(CarPartForm, self).__init__(*args, **kwargs)
		car_part_id = kwargs.get("instance").id
		
		if CarPartCar.objects.filter(car_part_id=car_part_id).values_list('car_id', flat=True).first():
			related_car_ids = CarPartCar.objects.filter(car_part_id=car_part_id).values_list("car_id")
			cars_with_car_part = Car.objects.filter(id__in=related_car_ids).values_list("model_name", flat=True)
			self.fields['expand_prices_to_cars_with_this_part'].help_text = "Cars with this CarPart: {}".format(', '.join(list(cars_with_car_part))) 
		else:
			self.fields['expand_prices_to_cars_with_this_part'].help_text = "There are no Cars that utilize this CarPart."
		
		
	expand_prices_to_cars_with_this_part = forms.BooleanField(required=False)
	class Meta:
		model = CarPart
		fields = '__all__'

	def clean(self):
		cleaned_data = super().clean()

		if cleaned_data.get('part_price') <= 0.00:
			raise forms.ValidationError("Part price must be greater than $0.00")

		self.cleaned_data['price_difference'] = cleaned_data.get('part_price') - CarPart.objects.filter(id=self.instance.id).values_list('part_price', flat=True).first()
		self.cleaned_data['cars_with_part'] = CarPartCar.objects.filter(car_part=self.instance.id).values_list('car', flat=True)

@admin.register(CarPart)
class CarPartAdmin(admin.ModelAdmin):
	form = CarPartForm
	search_fields = ('part_name',)
	
	def save_model(self, request, obj, form, change):
		if form.cleaned_data.get('expand_prices_to_cars_with_this_part'):
			# insert function here that you want to happen when the box is checked
			
			car_part_id = obj.id
			price_difference = form.cleaned_data.get('price_difference')
			cars_with_part = CarPartCar.objects.filter(car_part=car_part_id).values_list('car', flat=True)
			
			for car in form.cleaned_data.get('cars_with_part'):
				old_msrp = Car.objects.filter(id=car).values_list('msrp', flat=True)[0]
				Car.objects.filter(id=car).update(msrp=old_msrp+price_difference)

		super().save_model(request, obj, form, change)



@admin.register(CarPartCar)
class CarPartCarAdmin(admin.ModelAdmin):
	list_display = ('car_part', 'car',)
	search_fields = ('car_part', 'car_part__part_name', 'car', 'car__model_name',)