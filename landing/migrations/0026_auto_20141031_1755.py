# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0025_auto_20141014_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, verbose_name='T\xedtulo')),
                ('address', models.CharField(max_length=140, verbose_name='Direcci\xf3n')),
                ('room', models.CharField(max_length=140, verbose_name='Sal\xf3n')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripci\xf3n')),
                ('image', models.ImageField(upload_to=b'place/', verbose_name='Imagen')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ('is_partner', 'order')},
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='is_partner',
            field=models.BooleanField(default=True, verbose_name='Es aliado'),
        ),
    ]
