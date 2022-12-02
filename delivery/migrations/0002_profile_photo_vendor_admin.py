# Generated by Django 4.1.3 on 2022-12-01 18:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='photo'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='admin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vendor_approval', to='delivery.admin'),
        ),
    ]
