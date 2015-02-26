# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0027_placeinfo_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostEventPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'post/')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostEventVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_url', models.URLField(max_length=140)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='potentialsponsor',
            name='last_name',
            field=models.CharField(max_length=240, verbose_name='Nombres y apellidos'),
        ),
    ]
