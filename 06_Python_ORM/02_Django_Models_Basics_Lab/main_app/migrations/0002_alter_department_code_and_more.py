# Generated by Django 5.0.4 on 2024-06-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='employees_count',
            field=models.PositiveIntegerField(default=1, verbose_name='Employees count'),
        ),
    ]
