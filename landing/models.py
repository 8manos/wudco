# -*- coding:utf-8 -*-
from django.db import models

from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

from sorl.thumbnail import get_thumbnail


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
    workshop_name = models.CharField(max_length=200, verbose_name=u'Nombre del taller', blank=True)

    workshop_description = models.TextField(blank=True, verbose_name=u'Descripción del taller')
    workshop_learn = models.TextField(blank=True, verbose_name=u'Aprenderás',
                                      help_text='Separados con salto de línea.')

    workshop_image = models.ImageField(upload_to='taller/', blank=True, null=True)

    def get_workshoplearn_points(self):
        return [point for point in self.workshop_learn.split('\n') if point.strip()]

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('order', )


class Post(models.Model):
    date_published = models.DateTimeField(verbose_name=u'Fecha')
    title = models.CharField(max_length=140, verbose_name=u'Título')
    author = models.CharField(max_length=140, verbose_name=u'Autor')
    image = models.ImageField(upload_to='blog/')
    text = RichTextField(verbose_name=u'Contenido')
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False, verbose_name='Publicado')

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])

    def image_post(self):
        return get_thumbnail(self.image, '960x640').url

    def image_post_mini(self):
        return get_thumbnail(self.image, '96x64').url

    class Meta:
        ordering = ('-date_published', )


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


class PotentialSponsor(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=240, verbose_name=u'Asunto', default=u'Quiero ser patrocinador')
    last_name = models.CharField(max_length=240, verbose_name=u'Apellidos')
    email = models.EmailField(verbose_name=u'Correo electrónico')
    phone = models.CharField(max_length=240, verbose_name=u'Teléfono')
    company = models.CharField(max_length=240, verbose_name=u'Tu empresa / donde trabajas')
    comments = models.TextField(verbose_name=u'Comentarios', blank=True)
