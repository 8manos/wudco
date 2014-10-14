# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0024_pastedition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pastedition',
            options={'ordering': ('-year',)},
        ),
        migrations.AddField(
            model_name='sponsor',
            name='is_partner',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
