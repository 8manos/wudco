# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0021_agendaitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='only_workshop',
            field=models.BooleanField(default=False, verbose_name='S\xf3lo taller'),
            preserve_default=True,
        ),
    ]
