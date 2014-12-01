# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0004_auto_20141201_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(blank=True, max_length=17),
            preserve_default=True,
        ),
    ]
