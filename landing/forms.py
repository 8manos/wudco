# encoding:utf-8
from django import forms

from .models import PotentialSponsor
from django.utils.safestring import mark_safe


class SponsorForm(forms.ModelForm):
    error_css_class = 'field-error'
    required_css_class = 'field-required'
    terms = forms.BooleanField(required=True, label = mark_safe(u'Estoy de acuerdo con los <a href="#">términos de uso del sitio</a>'))

    def __init__(self, *args, **kwargs):
        super(SponsorForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['readonly'] = True
        # self.fields['subject'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = PotentialSponsor
