# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20141201_1854'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BookCategory',
        ),
    ]