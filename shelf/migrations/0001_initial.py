# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=20)),
                ('last_name', models.CharField(verbose_name='last name', max_length=50)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ('last_name', 'first_name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='shelf.Author')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='book category', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookEdition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('isbn', models.CharField(blank=True, max_length=17)),
                ('date', models.DateField()),
                ('book', models.ForeignKey(related_name='editions', to='shelf.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('catalogue_number', models.CharField(max_length=30)),
                ('cover', models.CharField(max_length=4, choices=[('soft', 'Soft'), ('hard', 'Hard')])),
                ('edition', models.ForeignKey(to='shelf.BookEdition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('url', models.CharField(max_length=250, default='http://www.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookedition',
            name='publisher',
            field=models.ForeignKey(to='shelf.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='shelf.BookCategory'),
            preserve_default=True,
        ),
    ]
