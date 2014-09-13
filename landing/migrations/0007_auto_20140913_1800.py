# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_speaker_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='bio',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='talk_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
