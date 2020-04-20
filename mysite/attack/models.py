from django.db import models
from sortedm2m.fields import SortedManyToManyField

class Categories(models.Model):
    id_category = models.AutoField(db_column='ID_Category', primary_key=True)  
    category = models.CharField(db_column='Category', max_length=100, verbose_name = "Categoria")  
    cat_description = models.TextField(db_column='CAT_Description', 
                                       max_length=500, verbose_name = "Descrizione")  

    def __str__(self):
        return self.category
        
    class Meta:
        managed = False
        verbose_name_plural = "Categorie"
        ordering = ['category']
        db_table = 'Categories'

#######################################################################################

class Values(models.Model):
    id_value = models.IntegerField(db_column='ID_Value', primary_key=True)  
    id_cat = models.ForeignKey(Categories, models.DO_NOTHING, db_column='ID_Cat',
                               verbose_name = "Categoria")
    value = models.CharField(db_column='Value', max_length=100, verbose_name = "Valore")
    descrizione = models.TextField(db_column='Descrizione', max_length=500, blank=True, null=True,
                                   verbose_name = "Descrizione")  

    def __str__(self):
        return self.value
    
    class Meta:
        managed = False
        ordering = ['id_value']
        verbose_name_plural = "Valori"
        db_table = 'Values'

#######################################################################################

class Attacks(models.Model):
    name = models.CharField(db_column='Name', max_length=100, verbose_name = "Nome")  
    atk_description = models.TextField(db_column='ATK_Description', max_length=500, 
                                       verbose_name = "Descrizione") 
    id_atk = models.AutoField(db_column='ID_ATK', primary_key=True) 
    valori_categoria = models.ManyToManyField(Values)
    #correlazione = SortedManyToManyField('Attacks')
    correlazione = models.ManyToManyField('Attacks')
    
    def __str__(self):
        return self.name

    
#     def get_absolute_url(self):
#         return reverse('model-detail-view', args=[str(self.id)])


    class Meta:
        ordering = ['name']
        verbose_name_plural = "Attacchi"
        db_table = 'Attacks'


#######################################################################################
#######################################################################################
#######################################################################################

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
