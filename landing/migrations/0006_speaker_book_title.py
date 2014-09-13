# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='book_title',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
