# Generated by Django 4.1 on 2022-09-01 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_alter_car_model_name_alter_car_msrp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=255)),
                ('part_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CarPartCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.car')),
                ('car_part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_parts.carpart')),
            ],
        ),
    ]
