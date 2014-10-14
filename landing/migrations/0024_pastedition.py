# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0023_nearbyplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastEdition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('youtube_id', models.CharField(max_length=300, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'past/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
