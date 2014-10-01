# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_auto_20140930_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='workshop_image',
        ),
        migrations.AddField(
            model_name='speaker',
            name='workshop_icon',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='\xcdcono del taller', choices=[(b'evaluation', b'Evaluaci\xc3\xb3n'), (b'execution', b'Ejecuci\xc3\xb3n'), (b'planning', b'Planeaci\xc3\xb3n')]),
            preserve_default=True,
        ),
    ]
