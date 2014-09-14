# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_speaker_workshop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='workshop_description',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
