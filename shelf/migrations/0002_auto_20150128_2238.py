# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookitem',
            old_name='cover',
            new_name='cover_type',
        ),
    ]
