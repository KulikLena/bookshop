# Generated by Django 4.0.6 on 2022-08-08 08:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_restriction', models.CharField(choices=[('Without restrictions', 'Without restrictions'), ('18+', '18+'), ('12+', '12+'), ('6+', '6+'), ('1+', '1+')], default='18+', max_length=20)),
            ],
        ),
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
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.CharField(choices=[('Hard cover', 'Hard cover'), ('Soft cover', 'Soft cover'), ('Other cover', 'Other')], default='Other cover', max_length=20)),
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
            name='Seria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField(default=10)),
                ('genre', models.CharField(choices=[('Nonfiction', (('Art/architecture', 'Art/architecture'), ('Autobiography', 'Autobiography'), ('Biography', 'Biography'), ('Business', 'Business/economics'), ('Crafts', 'Crafts/hobbies'), ('Cookbook', 'Cookbook'), ('Diary', 'Diary'), ('Dictionary', 'Dictionary'), ('Encyclopedia', 'Encyclopedia'), ('Guide', 'Guide'), ('Health', 'Health/fitness'), ('History', 'History'), ('Home', 'Home and garden'), ('Humor', 'Humor'), ('Journal', 'Journal'), ('MATH', 'Math'), ('Memoir', 'Memoir'), ('Philosophy', 'Philosophy'), ('Prayer', 'Prayer'), ('Religion', 'Religion, spirituality, and new age'), ('Textbook', 'Textbook'), ('True crime', 'True crime'), ('Review', 'Review'), ('Science', 'Science'), ('Self', 'Self help'), ('Sports', 'Sports and leisure'), ('Travel', 'Travel'), ('Other', 'Other'))), ('Fiction', (('Action', 'Action and adventure'), ('Alternate history', 'Alternate history'), ('Anthology', 'Anthology'), ('Chick lit', 'Chick lit'), ('Childrens', 'Childrens'), ('Classic', 'Classic'), ('Comic book', 'Comic book'), ('Coming-of-age', 'Coming-of-age'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fairytale', 'Fairytale'), ('Fantasy', 'Fantasy'), ('Graphic novel', 'Graphic novel'), ('Historical fiction', 'Historical fiction'), ('Mystery', 'Horror'), ('Comic book', 'Mystery'), ('Paranormal romance', 'Paranormal romance'), ('Picture book', 'Picture book'), ('Poetry', 'Poetry'), ('Political thriller', 'Political thriller'), ('Romance', 'Romance'), ('Satire', 'Satire'), ('Science fiction', 'Science fiction'), ('Short story', 'Short story'), ('Suspense', 'Suspense'), ('Thriller', 'Thriller'), ('Thriller', 'Western'), ('Young adult', 'Young adult'), ('Other', 'Other'))), ('unknown', 'Unknown')], max_length=120)),
                ('pages', models.IntegerField(default=0)),
                ('cover', models.CharField(choices=[('Hard cover', 'Hard cover'), ('Soft cover', 'Soft cover'), ('Other cover', 'Other')], default='Other', max_length=120)),
                ('format', models.IntegerField(blank=True, help_text='Please use the following format: width(cm) x length(cm): ', null=True)),
                ('date_published', models.DateField(default=datetime.date(1990, 1, 1))),
                ('isbn', models.CharField(default='000-000-0000-00-0', max_length=40)),
                ('weight', models.CharField(default='0', max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('age_restriction', models.CharField(choices=[('Without restrictions', 'Without restrictions'), ('18+', '18+'), ('12+', '12+'), ('6+', '6+'), ('1+', '1+')], default='18+', max_length=402)),
                ('items_available', models.IntegerField(default=0)),
                ('order_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=40)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 8, 8, 11, 21, 52, 584885), editable=False)),
                ('modified', models.DateTimeField(default=datetime.datetime(2022, 8, 8, 11, 21, 52, 584885))),
                ('authors', models.ManyToManyField(to='forecast.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forecast.publisher')),
                ('seria', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='forecast.seria')),
            ],
        ),
    ]
