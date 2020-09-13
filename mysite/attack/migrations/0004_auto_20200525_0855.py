# Generated by Django 3.0.5 on 2020-05-25 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attack', '0003_auto_20200525_0851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='names',
            options={'ordering': ['name'], 'verbose_name_plural': 'Nomi alternativi'},
        ),
        migrations.AddField(
            model_name='names',
            name='id_atk',
            field=models.ForeignKey(blank=True, db_column='id_atk', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attack.Attacks', verbose_name='Attacco principale'),
        ),
    ]