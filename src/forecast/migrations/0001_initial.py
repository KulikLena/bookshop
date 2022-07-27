# Generated by Django 4.0.6 on 2022-07-26 22:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(default=datetime.date(1, 1, 1))),
                ('death_date', models.DateField(blank=True, null=True)),
                ('country_of_birth', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('native_language_book_title', models.CharField(max_length=50)),
                ('first_published', models.DateField(default=datetime.date(1990, 1, 1))),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('Nonfiction', (('Art/architecture', 'Art/architecture'), ('Autobiography', 'Autobiography'), ('Biography', 'Biography'), ('Business', 'Business/economics'), ('Crafts', 'Crafts/hobbies'), ('Cookbook', 'Cookbook'), ('Diary', 'Diary'), ('Dictionary', 'Dictionary'), ('Encyclopedia', 'Encyclopedia'), ('Guide', 'Guide'), ('Health', 'Health/fitness'), ('History', 'History'), ('Home', 'Home and garden'), ('Humor', 'Humor'), ('Journal', 'Journal'), ('MATH', 'Math'), ('Memoir', 'Memoir'), ('Philosophy', 'Philosophy'), ('Prayer', 'Prayer'), ('Religion', 'Religion, spirituality, and new age'), ('Textbook', 'Textbook'), ('True crime', 'True crime'), ('Review', 'Review'), ('Science', 'Science'), ('Self', 'Self help'), ('Sports', 'Sports and leisure'), ('Travel', 'Travel'), ('Other', 'Other'))), ('Fiction', (('Action', 'Action and adventure'), ('Alternate history', 'Alternate history'), ('Anthology', 'Anthology'), ('Chick lit', 'Chick lit'), ('Childrens', 'Childrens'), ('Classic', 'Classic'), ('Comic book', 'Comic book'), ('Coming-of-age', 'Coming-of-age'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fairytale', 'Fairytale'), ('Fantasy', 'Fantasy'), ('Graphic novel', 'Graphic novel'), ('Historical fiction', 'Historical fiction'), ('Mystery', 'Horror'), ('Comic book', 'Mystery'), ('Paranormal romance', 'Paranormal romance'), ('Picture book', 'Picture book'), ('Poetry', 'Poetry'), ('Political thriller', 'Political thriller'), ('Romance', 'Romance'), ('Satire', 'Satire'), ('Science fiction', 'Science fiction'), ('Short story', 'Short story'), ('Suspense', 'Suspense'), ('Thriller', 'Thriller'), ('Thriller', 'Western'), ('Young adult', 'Young adult'), ('Other', 'Other'))), ('unknown', 'Unknown')], default='Other', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
       
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Nonfiction', (('Art/architecture', 'Art/architecture'), ('Autobiography', 'Autobiography'), ('Biography', 'Biography'), ('Business', 'Business/economics'), ('Crafts', 'Crafts/hobbies'), ('Cookbook', 'Cookbook'), ('Diary', 'Diary'), ('Dictionary', 'Dictionary'), ('Encyclopedia', 'Encyclopedia'), ('Guide', 'Guide'), ('Health', 'Health/fitness'), ('History', 'History'), ('Home', 'Home and garden'), ('Humor', 'Humor'), ('Journal', 'Journal'), ('MATH', 'Math'), ('Memoir', 'Memoir'), ('Philosophy', 'Philosophy'), ('Prayer', 'Prayer'), ('Religion', 'Religion, spirituality, and new age'), ('Textbook', 'Textbook'), ('True crime', 'True crime'), ('Review', 'Review'), ('Science', 'Science'), ('Self', 'Self help'), ('Sports', 'Sports and leisure'), ('Travel', 'Travel'), ('Other', 'Other'))), ('Fiction', (('Action', 'Action and adventure'), ('Alternate history', 'Alternate history'), ('Anthology', 'Anthology'), ('Chick lit', 'Chick lit'), ('Childrens', 'Childrens'), ('Classic', 'Classic'), ('Comic book', 'Comic book'), ('Coming-of-age', 'Coming-of-age'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fairytale', 'Fairytale'), ('Fantasy', 'Fantasy'), ('Graphic novel', 'Graphic novel'), ('Historical fiction', 'Historical fiction'), ('Mystery', 'Horror'), ('Comic book', 'Mystery'), ('Paranormal romance', 'Paranormal romance'), ('Picture book', 'Picture book'), ('Poetry', 'Poetry'), ('Political thriller', 'Political thriller'), ('Romance', 'Romance'), ('Satire', 'Satire'), ('Science fiction', 'Science fiction'), ('Short story', 'Short story'), ('Suspense', 'Suspense'), ('Thriller', 'Thriller'), ('Thriller', 'Western'), ('Young adult', 'Young adult'), ('Other', 'Other'))), ('unknown', 'Unknown')], max_length=20)),
                ('date_published', models.DateField(default=datetime.date(1990, 1, 1))),
                ('authors', models.ManyToManyField(to='forecast.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.publisher')),
            ],
        ),
    ]
