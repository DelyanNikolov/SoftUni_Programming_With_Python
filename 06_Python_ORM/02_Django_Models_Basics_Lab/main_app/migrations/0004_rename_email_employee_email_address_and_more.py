# Generated by Django 5.0.4 on 2024-06-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_department_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='email_address',
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
