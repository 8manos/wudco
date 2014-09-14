# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_speaker_workshop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='workshop_learn',
            field=models.TextField(default='', verbose_name='Aprender\xe1s', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='speaker',
            name='bio',
            field=models.TextField(verbose_name='Biograf\xeda', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='book_title',
            field=models.CharField(max_length=200, verbose_name='T\xedtulo de libro', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='picture',
            field=models.ImageField(upload_to=b'speaker/', verbose_name='Im\xe1gen'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='talk_name',
            field=models.CharField(max_length=200, verbose_name='Nombre de la charla'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='url',
            field=models.URLField(verbose_name='Enlace web', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='workshop_description',
            field=models.TextField(verbose_name='Descripci\xf3n del taller', blank=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='workshop_name',
            field=models.CharField(max_length=200, verbose_name='Nombre del taller'),
        ),
    ]
