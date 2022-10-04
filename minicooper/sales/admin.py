from django.contrib import admin
from .models import Sale

# Register your models here.
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
	list_display = ('car', 'sale_price', 'sale_date', )
	search_fields = ('sale_date', )

	# def get_search_results(self, request, queryset, search_term):
	# 	use_distinct = False
	# 	if not search_term:
	# 		return queryset, use_distinct
	# 	else:
	# 		return self.model.objects.filter(your filters here using search_term), use_distinct