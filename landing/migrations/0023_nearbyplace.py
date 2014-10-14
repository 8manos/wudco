# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0022_speaker_only_workshop'),
    ]

    operations = [
        migrations.CreateModel(
            name='NearbyPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_type', models.IntegerField(choices=[(0, 'Restaurantes cerca'), (1, 'Transporte'), (2, 'Informaci\xf3n pr\xe1ctica')])),
                ('name', models.CharField(max_length=300)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('place_type', 'order'),
            },
            bases=(models.Model,),
        ),
    ]
