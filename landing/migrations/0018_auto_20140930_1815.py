# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0017_auto_20140929_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='workshop_image',
            field=models.ImageField(null=True, upload_to=b'taller/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='speaker',
            name='workshop_name',
            field=models.CharField(max_length=200, verbose_name='Nombre del taller', blank=True),
        ),
    ]
