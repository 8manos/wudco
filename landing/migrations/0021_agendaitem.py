# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0020_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, verbose_name='T\xedtulo')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('item_type', models.CharField(max_length=140, verbose_name='\xedcono', choices=[(b'clock', 'Reloj'), (b'evaluation', 'Evaluaci\xf3n'), (b'execution', 'Ejecuci\xf3n'), (b'planning', 'Planeaci\xf3n')])),
                ('time_starts', models.TimeField(db_index=True)),
                ('time_ends', models.TimeField()),
                ('coffee_break_after', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('time_starts',),
            },
            bases=(models.Model,),
        ),
    ]
