# Generated by Django 4.1.2 on 2022-11-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_room_service_image_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='update_category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
