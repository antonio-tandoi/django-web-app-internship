from django.contrib import admin
from .models import Attacks, Categories, Values
#from advanced_filters.admin import AdminAdvancedFiltersMixin
from autocompletefilter.admin import AutocompleteFilterMixin
from autocompletefilter.filters import AutocompleteListFilter
from django.contrib.admin import site
import adminactions.actions as actions

# register all adminactions
actions.add_to_site(site)

admin.site.site_header = 'Pannello di amministrazione'
admin.site.site_title = 'Admin'
admin.site.index_title = "Dashboard"


class AttacksAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
	
	def display_value_1(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[:1])
	display_value_1.short_description = 'Attivo/Passivo'
	
	def display_value_2(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[1:2])
	display_value_2.short_description = 'TCP/IP Layer'
	
	def display_value_3(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[2:3])
	display_value_3.short_description = 'Exploit'
	
	def display_value_4(self,object):
		return ','.join(v.value for v in object.valori_categoria.all()[3:4])
	display_value_4.short_description = 'Tipologia'
	
	
	list_display = ('name', 'display_value_3', 
				'display_value_4')
	list_filter = (('valori_categoria', AutocompleteListFilter),)
	search_fields = ['name', 'atk_description']
	fields = ['name', 'atk_description', 'valori_categoria','correlazione']
	list_per_page = 30
	show_full_result_count = True
	#raw_id_fields = ('correlazione',)
	
	icon_name = 'report_problem' 

admin.site.register(Attacks, AttacksAdmin)

#######################################################################################

class ValuesAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
	list_display = ('value', 'descrizione')
	list_filter = (('id_cat', AutocompleteListFilter),)
	search_fields = ['value'] 
	fields = ['value','descrizione', 'id_cat']
	
	icon_name = 'settings_input_component' 
	
admin.site.register(Values, ValuesAdmin)

#######################################################################################

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'cat_description')
	search_fields = ['category', 'cat_description']
	
	icon_name = 'receipt'
	
admin.site.register(Categories, CategoriesAdmin)

