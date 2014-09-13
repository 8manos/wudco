# -*- coding:utf-8 -*-
from django.db import models


class Speaker(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    company = models.CharField(max_length=140, verbose_name=u'Organización')
    picture = models.ImageField(upload_to='speaker/')
    title = models.CharField(max_length=140, verbose_name=u'Descripción')
    url = models.URLField(max_length=200, blank=True)
    book_title = models.CharField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    talk_name = models.CharField(max_length=200)
    workshop_name = models.CharField(max_length=200)

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
