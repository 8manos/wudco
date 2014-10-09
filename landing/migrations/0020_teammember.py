# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_auto_20141001_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('picture', models.ImageField(upload_to=b'speaker/', verbose_name='Im\xe1gen')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
    ]
