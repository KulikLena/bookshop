# Generated by Django 4.0.6 on 2022-07-24 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_remove_book_author_book_authors_alter_book_publisher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native_language_book_title', models.CharField(max_length=50)),
                ('first_published', models.DateField(default=datetime.date(1990, 1, 1))),
            ],
        ),
    ]
