# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0028_auto_20150226_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteventphoto',
            name='name',
            field=models.TextField(default='nombre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posteventvideo',
            name='name',
            field=models.TextField(default='nombre video'),
            preserve_default=False,
        ),
    ]
