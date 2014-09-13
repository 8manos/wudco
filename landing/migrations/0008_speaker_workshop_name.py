# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20140913_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='workshop_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
