# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0005_auto_20141201_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'book', 'ordering': ['title'], 'verbose_name_plural': 'books'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='name',
            field=models.CharField(verbose_name='book category', max_length=100),
            preserve_default=True,
        ),
    ]
