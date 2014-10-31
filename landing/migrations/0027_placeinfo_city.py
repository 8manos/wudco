# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0026_auto_20141031_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeinfo',
            name='city',
            field=models.CharField(default='Bogota', max_length=140, verbose_name='Ciudad'),
            preserve_default=False,
        ),
    ]
