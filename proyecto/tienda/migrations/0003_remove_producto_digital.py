# Generated by Django 4.0.6 on 2023-04-22 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20220706_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='digital',
        ),
    ]
