# Generated by Django 5.1.2 on 2024-10-20 10:24

import WorldOfSpeedApp.cars.custom_validators
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open_Wheel', 'Open_Wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.IntegerField(validators=[WorldOfSpeedApp.cars.custom_validators.YearValidator(1999, 2030)])),
                ('image_url', models.URLField(unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
