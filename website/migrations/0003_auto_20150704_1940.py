# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150704_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='star',
            name='country',
            field=models.ForeignKey(verbose_name=b'Pa\xc3\xads', blank=True, to='website.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='star',
            name='photo',
            field=models.ImageField(default=None, upload_to=b'uploads/star/%Y/%m/', verbose_name=b'Foto'),
            preserve_default=False,
        ),
    ]
