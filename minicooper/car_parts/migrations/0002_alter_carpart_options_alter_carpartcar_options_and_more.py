# Generated by Django 4.1 on 2022-10-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_parts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carpart',
            options={'verbose_name': 'Car Part'},
        ),
        migrations.AlterModelOptions(
            name='carpartcar',
            options={'verbose_name': 'Car Parts Car'},
        ),
        migrations.AlterField(
            model_name='carpart',
            name='part_name',
            field=models.CharField(max_length=255, verbose_name='Part Name'),
        ),
        migrations.AlterField(
            model_name='carpart',
            name='part_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Part Price'),
        ),
        migrations.AlterField(
            model_name='carpartcar',
            name='car_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_parts.carpart', verbose_name='Car Part'),
        ),
    ]
