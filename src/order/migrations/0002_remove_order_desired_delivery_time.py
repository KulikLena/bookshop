# Generated by Django 4.0.6 on 2022-08-22 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='desired_delivery_time',
        ),
    ]
