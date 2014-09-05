# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField()),
                ('name', models.CharField(max_length=140)),
                ('speaker_name', models.CharField(max_length=140)),
                ('url', models.URLField(max_length=140, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
