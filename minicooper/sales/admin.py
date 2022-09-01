from django.contrib import admin
from .models import Sale

# Register your models here.
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
	list_display = ('car', 'sale_price', 'sale_date', )
	search_fields = ('sale_date', )