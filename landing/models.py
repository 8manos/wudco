# -*- coding:utf-8 -*-
from django.db import models


class Speaker(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    company = models.CharField(max_length=140, verbose_name=u'Organización')
    picture = models.ImageField(upload_to='speaker/', verbose_name=u'Imágen')
    title = models.CharField(max_length=140, verbose_name=u'Descripción')
    url = models.URLField(max_length=200, blank=True, verbose_name=u'Enlace web')
    book_title = models.CharField(max_length=200, blank=True, verbose_name=u'Título de libro')
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True, verbose_name=u'Biografía')

    talk_name = models.CharField(max_length=200, verbose_name=u'Nombre de la charla')
    workshop_name = models.CharField(max_length=200, verbose_name=u'Nombre del taller')

    workshop_description = models.TextField(blank=True, verbose_name=u'Descripción del taller')
    workshop_learn = models.TextField(blank=True, verbose_name=u'Aprenderás',
                                      help_text='Separados con salto de línea.')

    def get_workshoplearn_points(self):
        return [point for point in self.workshop_learn.split('\n') if point.strip()]

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('order', )


class Sponsor(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    url = models.URLField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='sponsor/')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('order', )


class Talk(models.Model):
    when = models.DateTimeField()
    name = models.CharField(max_length=140)
    speaker_name = models.CharField(max_length=140)
    url = models.URLField(max_length=140, blank=True)
