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
	
	'''
	1 - 3  : Attivo/Passivo
	4 - 7  : TCP/IP Layer - 19: None
	8 - 10 : Exploit
	11 - 18: Tipology
	20 - 22: CIA Triad
	23 - 25: Difficoltà
	'''
	
	def display_value_1(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if element.id_value <= 3:
				return element.value	
	display_value_1.short_description = 'Attivo/Passivo'
  	
	def display_value_2(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if (element.id_value >= 4 and element.id_value <= 7) or element.id_value == 19:
				return element.value
	display_value_2.short_description = 'TCP/IP Layer'
   	
	def display_value_3(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if (element.id_value >= 8 and element.id_value <= 10):
				return element.value
	display_value_3.short_description = 'Exploit'
    	
	def display_value_4(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if (element.id_value >= 11 and element.id_value <= 18):
				return element.value
		#return ','.join(v.value for v in object.valori_categoria.all()[3:4])
	display_value_4.short_description = 'Tipologia'
	
	def display_value_5(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if (element.id_value >= 20 and element.id_value <= 22):
				return element.value
		#return ','.join(v.value for v in object.valori_categoria.all()[3:4])
	display_value_5.short_description = 'CIA triad'
	
	def display_value_6(self,object):
		mylist = []
		for v in object.valori_categoria.all():
			mylist.append(v)
		for element in mylist:
			if (element.id_value >= 23 and element.id_value <= 25):
				return element.value
		#return ','.join(v.value for v in object.valori_categoria.all()[3:4])
	display_value_6.short_description = 'Difficoltà'
	
	def display_correlation(self, object):
		mylist = []
		for a in object.correlazione.all():
			mylist.append(a)
		if len(mylist) == 0:
			return "None"
		return "\n".join([a.name for a in object.correlazione.filter()])
	display_correlation.short_description = "Correlazione"
				
	'''
	Di default, il link per modificare l'oggetto è posto sul primo elemento di list_display;
	Usare list_display_links per selezionare quali field devono avere il link
	'''
	list_display = ('name', 'display_value_2', 'display_value_4',)
	list_filter = (('valori_categoria', AutocompleteListFilter),)
	search_fields = ['name', 'atk_description', 'otherNames']
	fields = ['name', 'atk_description', 'otherNames', 'valori_categoria', 'correlazione', ]
	filter_horizontal = ('correlazione',)
	list_per_page = 30
	show_full_result_count = True
	#raw_id_fields = ('correlazione',)
	
	icon_name = 'report_problem' 

admin.site.register(Attacks, AttacksAdmin)

#######################################################################################

class ValuesAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
	list_display = ('value', 'descrizione', 'categoryName')
	list_filter = (('id_category', AutocompleteListFilter),)
	search_fields = ['value'] 
	fields = ('value', 'id_category','descrizione')
	
	icon_name = 'settings_input_component' 
	
	def categoryName(self, instance):
		return instance.id_category.category
	categoryName.short_description = "Categoria"
	
admin.site.register(Values, ValuesAdmin)

#######################################################################################

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'cat_description')
	search_fields = ['category', 'cat_description']
	field = ['category', 'cat_description',]
	
	icon_name = 'receipt'
	
admin.site.register(Categories, CategoriesAdmin)

