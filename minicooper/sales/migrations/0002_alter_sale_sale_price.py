# Generated by Django 4.1 on 2022-09-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sale Price'),
        ),
    ]