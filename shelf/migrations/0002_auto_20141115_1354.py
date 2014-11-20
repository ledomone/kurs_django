# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='publisher',
            name='url',
            field=models.CharField(default='http://www.', max_length=250),
            preserve_default=True,
        ),
    ]
