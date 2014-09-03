# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('picture', models.ImageField(upload_to=b'speaker/')),
                ('title', models.CharField(max_length=140, verbose_name='Descripci\xf3n')),
                ('twitter_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
