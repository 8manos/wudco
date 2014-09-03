# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20140903_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='company',
            field=models.CharField(default='', max_length=140, verbose_name='Organizaci\xf3n'),
            preserve_default=False,
        ),
    ]
