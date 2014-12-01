# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20141125_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedition',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 12, 1, 17, 53, 19, 609048, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='catalogue_number',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
    ]
