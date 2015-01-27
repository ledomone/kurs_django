# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141228_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibliouser',
            options={'permissions': (('can_rent', 'użytkownik może wypożyczać książki'),)},
        ),
    ]
