# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_remove_potentialsponsor_terms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_published', models.DateTimeField(verbose_name='Fecha')),
                ('title', models.CharField(max_length=140, verbose_name='T\xedtulo')),
                ('author', models.CharField(max_length=140, verbose_name='Autor')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Contenido')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
