# Generated by Django 5.0.4 on 2024-06-18 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_email_employee_email_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='last_edited',
            new_name='last_edited_on',
        ),
    ]
