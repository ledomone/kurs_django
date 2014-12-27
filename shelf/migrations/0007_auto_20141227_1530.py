# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0006_auto_20141201_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book', related_name='editions'),
            preserve_default=True,
        ),
    ]
