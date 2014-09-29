# encoding:utf-8
from django import forms

from .models import PotentialSponsor
from django.utils.safestring import mark_safe


class SponsorForm(forms.ModelForm):
    error_css_class = 'field-error'
    required_css_class = 'field-required'
    terms = forms.BooleanField(required=True, label = mark_safe(u'Estoy de acuerdo con los <a href="#">términos de uso del sitio</a>'))

    class Meta:
        model = PotentialSponsor
