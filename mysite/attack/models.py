from django.db import models

class Categories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    category = models.CharField(db_column='Category', max_length=100, verbose_name = "Categoria", 
                                blank=True, null=True)  
    cat_description = models.TextField(db_column='CAT_DESCRIPTION', blank=True, null=True,
                                       max_length=100, verbose_name = "Descrizione") 
    
    def __str__(self):
        return self.category
        
    class Meta:
        verbose_name_plural = "Categorie"
        ordering = ['category']
        db_table = 'Categories'

#######################################################################################

class Values(models.Model):    
    id_value = models.AutoField(db_column='ID_Value', primary_key=True)
    value = models.CharField(db_column='Value', max_length=100, blank=True, null=True, 
                             verbose_name = "Valore")  
    descrizione = models.TextField(db_column='Descrizione', max_length=500, blank=True, null=True, verbose_name = "Descrizione")
    id_category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='ID_CATEGORY', 
                                    blank=True, null=True, verbose_name = "Categoria") 

  

    def __str__(self):
        return self.value
    
    class Meta:
        ordering = ['id_value']
        verbose_name_plural = "Valori"
        db_table = 'Values'

#######################################################################################

class Attacks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True, 
                            verbose_name = "Nome") 
    atk_description = models.TextField(db_column='ATK_Description', max_length=500, blank=True, null=True,
                                       verbose_name = "Descrizione")
    otherNames = models.TextField(db_column='OtherNames', max_length=100, blank=True, null=True,
                                       verbose_name = "Nomi Alternativi")
    valori_categoria = models.ManyToManyField(Values)
    correlazione = models.ManyToManyField('Attacks', blank = True) 

    class Meta:
        verbose_name_plural = "Attacchi"
        db_table = 'Attacks' 
        ordering = ['name']  
    
    def __str__(self):
        return self.name
    
#######################################################################################



