# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('returned', models.DateTimeField(blank=True, null=True)),
                ('what', models.ForeignKey(to='shelf.BookItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
