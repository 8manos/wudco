# encoding:utf-8
from django import forms
from django.utils.safestring import mark_safe

class SponsorForm(forms.Form):
	#auto_id = '%s'
	#label_suffix = ''
	error_css_class = 'field-error'
	required_css_class = 'field-required'
	subject = forms.CharField(label = u'Asunto', initial = u'Quiero ser patrocinador')
	last_name = forms.CharField(label = u'Apellidos')
	email = forms.EmailField(label = u'Correo electrónico')
	phone = forms.CharField(label = u'Teléfono')
	company = forms.CharField(label = u'Tu empresa / donde trabajas')
	comments = forms.CharField(widget = forms.Textarea, label = u'Comentarios', required = False)
	terms = forms.BooleanField(label = mark_safe(u'Estoy de acuerdo con los <a href="#">términos de uso del sitio</a>'))