# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_rental_who'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'permissions': (('can_rent', 'User can rent a book'),)},
        ),
    ]
