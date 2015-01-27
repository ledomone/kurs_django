# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20150127_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'permissions': (('can_rent', 'Can rent a book'),)},
        ),
    ]
