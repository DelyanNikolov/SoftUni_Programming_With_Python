# Generated by Django 5.0.4 on 2024-07-15 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_restaurantreview_regularrestaurantreview_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Food Critic Review', 'verbose_name_plural': 'Food Critic Reviews'},
        ),
        migrations.AlterModelOptions(
            name='regularrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Restaurant Review', 'verbose_name_plural': 'Restaurant Reviews'},
        ),
    ]