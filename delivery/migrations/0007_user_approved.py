# Generated by Django 4.1.3 on 2022-12-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_remove_rider_approval_remove_rider_mobile_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]