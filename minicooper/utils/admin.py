from django.contrib import admin

class DevCustomModelAdmin(CustomModelAdmin):
	'''
	Use this ModelAdmin when you want to use the 'dev' database 
	'''
	# A handy constant for the name of the alternate database
	using = 'dev'

	def save_model(self, request, obj, form, change):
		# Tell Django to save objects to the 'dev' database
		obj.save(using=self.using)

	def delete_model(self, request, obj):
		# Tell Django to delete objects from the 'dev' database
		obj.delete(using=self.using)

	def get_queryset(self, request):
		# Tell Django to look for objects in the 'dev' database
		return super().get_queryset(request).using(self.using)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		# Tell Django to populate ForeignKey widgets using a query
		# on the 'dev' database
		return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

	def formfield_for_manytomany(self, db_field, request, **kwargs):
		# Tell Django to populate ManyToMany widgets using a query
		# on the 'dev' database
		return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)