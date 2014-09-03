# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='speaker',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speaker',
            name='url',
            field=models.URLField(default='#', blank=True),
            preserve_default=False,
        ),
    ]
