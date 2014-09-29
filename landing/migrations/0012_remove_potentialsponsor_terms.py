# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20140929_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potentialsponsor',
            name='terms',
        ),
    ]
