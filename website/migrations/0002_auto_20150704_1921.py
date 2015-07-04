# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gender',
            name='status',
            field=models.BooleanField(default=True, verbose_name=b'Ativo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='star',
            name='status',
            field=models.BooleanField(default=True, verbose_name=b'Ativo'),
            preserve_default=True,
        ),
    ]
