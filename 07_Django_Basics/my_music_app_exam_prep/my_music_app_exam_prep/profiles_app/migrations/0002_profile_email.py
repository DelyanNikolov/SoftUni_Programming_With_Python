# Generated by Django 5.1.2 on 2024-10-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='delian@abv.bg', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
