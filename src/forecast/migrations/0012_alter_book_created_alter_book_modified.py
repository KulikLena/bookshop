# Generated by Django 4.0.6 on 2022-08-20 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0011_alter_book_created_alter_book_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 26, 834963), editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 22, 48, 26, 834963)),
        ),
    ]