# Generated by Django 4.1.3 on 2022-11-28 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_room_breakfast_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='breakfast_price',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price_with_AC',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price_without_AC',
        ),
    ]
