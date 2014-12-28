# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliouser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bibliouser',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=True,
        ),
    ]
