# Generated by Django 4.1.3 on 2022-11-24 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='last_names',
            new_name='last_name',
        ),
    ]