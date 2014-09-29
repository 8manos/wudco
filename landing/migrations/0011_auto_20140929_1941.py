# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20140914_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialSponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(default='Quiero ser patrocinador', max_length=240, verbose_name='Asunto')),
                ('last_name', models.CharField(max_length=240, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=75, verbose_name='Correo electr\xf3nico')),
                ('phone', models.CharField(max_length=240, verbose_name='Tel\xe9fono')),
                ('company', models.CharField(max_length=240, verbose_name='Tu empresa / donde trabajas')),
                ('comments', models.TextField(verbose_name='Comentarios', blank=True)),
                ('terms', models.BooleanField(verbose_name='Estoy de acuerdo con los <a href="#">t\xe9rminos de uso del sitio</a>')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='workshop_learn',
            field=models.TextField(help_text=b'Separados con salto de l\xc3\xadnea.', verbose_name='Aprender\xe1s', blank=True),
        ),
    ]
