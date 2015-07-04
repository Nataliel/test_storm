# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, help_text=b'Data em que este filme foi cadastrado', verbose_name=b'Data do Cadastro', blank=True)),
            ],
            options={
                'ordering': ('created_at',),
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Titulo do filme, no maximo 100 caracteres.', max_length=100, verbose_name=b'T\xc3\xadtulo')),
                ('photo', models.ImageField(upload_to=b'uploads/movie/%Y/%m/', verbose_name=b'Foto')),
                ('trailer', models.CharField(help_text=b'Endere\xc3\xa7o do Youtube', max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('synopsis', models.TextField(verbose_name=b'Sinopse')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, help_text=b'Data em que este filme foi cadastrado', verbose_name=b'Data do Cadastro', blank=True)),
                ('status', models.BooleanField(default=True, help_text=b'Se est\xc3\xa1 em cartaz ou n\xc3\xa3o.', verbose_name=b'Cartaz')),
                ('gender', models.ManyToManyField(to='website.Gender', verbose_name=b'Genero do filme')),
            ],
            options={
                'ordering': ('created_at',),
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, help_text=b'Data em que este filme foi cadastrado', verbose_name=b'Data do Cadastro', blank=True)),
            ],
            options={
                'ordering': ('created_at',),
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.ManyToManyField(help_text=b'Elenco do filme', to='website.Star', max_length=300),
            preserve_default=True,
        ),
    ]
