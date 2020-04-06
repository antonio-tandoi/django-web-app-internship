from django.contrib import admin
from .models import Attacks, Categories, Values


admin.site.site_header = 'Pannello di amministrazione'
admin.site.site_title = 'Admin'
admin.site.index_title = "Dashboard"


class AttacksAdmin(admin.ModelAdmin):
	
	def display_value_1(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[:1])
	display_value_1.short_description = 'Attivo/Passivo'
	
	def display_value_2(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[1:2])
	display_value_2.short_description = 'TCP/IP Layer'
	
	def display_value_3(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[2:3])
	display_value_3.short_description = 'Exploit'
	
	
	list_display = ('name', 'display_value_1', 
				'display_value_2', 'display_value_3')
	list_filter = ('valori_categoria',)
	search_fields = ['name', 'atk_description']
	fields = ['name', 'atk_description', ('valori_categoria','correlazione')]
	list_per_page = 20
	show_full_result_count = True

admin.site.register(Attacks, AttacksAdmin)

#######################################################################################

class ValuesAdmin(admin.ModelAdmin):
	list_display = ('value', 'id_cat')
	list_filter = ('id_cat',)
	search_fields = ['value'] 
	fields = ['value', 'id_cat']
	
admin.site.register(Values, ValuesAdmin)

#######################################################################################

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'cat_description')
	search_fields = ['category', 'cat_description']
admin.site.register(Categories, CategoriesAdmin)

